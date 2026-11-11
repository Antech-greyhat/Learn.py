
from pathlib import Path
import argparse
import secrets

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


BASE = Path(__file__).resolve().parent / "crypto_lab"

SAMPLES = BASE / "samples"
ENCRYPTED = BASE / "encrypted"
RECOVERED = BASE / "recovered"
KEY_FILE = BASE / "secret.key"

SAMPLE_NAMES = [
    "sample1.txt",
    "sample2.txt",
    "sample3.txt",
]


def initialize():
    """Create disposable sample files."""
    for folder in (SAMPLES, ENCRYPTED, RECOVERED):
        folder.mkdir(parents=True, exist_ok=True)

    examples = {
        "sample1.txt": "Cryptography laboratory: document one.",
        "sample2.txt": "Cryptography laboratory: document two.",
        "sample3.txt": "Cryptography laboratory: document three."
    }

    for name, content in examples.items():
        path = SAMPLES / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    if not KEY_FILE.exists():
        KEY_FILE.write_bytes(AESGCM.generate_key(bit_length=256))

    print("[+] Laboratory initialized.")
    print(f"[+] Samples: {SAMPLES}")


def load_key():
    if not KEY_FILE.exists():
        raise FileNotFoundError("Laboratory key not found.")

    key = KEY_FILE.read_bytes()

    if len(key) != 32:
        raise ValueError("Invalid AES-256 key.")

    return key


def encrypt():
    """Encrypt copies of the predefined sample files."""
    aes = AESGCM(load_key())

    for name in SAMPLE_NAMES:
        source = SAMPLES / name
        destination = ENCRYPTED / f"{name}.enc"

        if not source.is_file():
            continue

        if destination.exists():
            print(f"[!] Already encrypted: {name}")
            continue

        plaintext = source.read_bytes()
        nonce = secrets.token_bytes(12)

        
        aad = name.encode("utf-8")

        ciphertext = aes.encrypt(nonce, plaintext, aad)

        
        destination.write_bytes(nonce + ciphertext)

        print(f"[+] Encrypted copy: {destination.name}")

    print("[+] Original samples remain untouched.")


def decrypt():
    """Authenticate and recover encrypted copies."""
    aes = AESGCM(load_key())

    for name in SAMPLE_NAMES:
        source = ENCRYPTED / f"{name}.enc"
        destination = RECOVERED / name

        if not source.is_file():
            continue

        if destination.exists():
            print(f"[!] Recovery file already exists: {name}")
            continue

        blob = source.read_bytes()

        if len(blob) < 28:
            print(f"[-] Invalid encrypted file: {name}")
            continue

        nonce = blob[:12]
        ciphertext = blob[12:]
        aad = name.encode("utf-8")

        try:
            plaintext = aes.decrypt(nonce, ciphertext, aad)
            destination.write_bytes(plaintext)

            print(f"[+] Recovered: {name}")

        except Exception:
            print(f"[-] Authentication failed: {name}")

    print("[+] Recovery operation completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Isolated AES-256-GCM cryptography laboratory"
    )

    parser.add_argument(
        "action",
        choices=["init", "encrypt", "decrypt"]
    )

    args = parser.parse_args()

    if args.action == "init":
        initialize()
    elif args.action == "encrypt":
        encrypt()
    elif args.action == "decrypt":
        decrypt()


if __name__ == "__main__":
    main()
