import os
import argparse
from pathlib import Path
from cryptography.fernet import Fernet

LAB = Path("ransomware_lab")
KEY_FILE = LAB / "recovery.key"
NOTE_FILE = LAB / "README_RECOVERY.txt"


def initialize():
    LAB.mkdir(exist_ok=True)

    (LAB / "document.txt").write_text(
        "Confidential laboratory document.\n"
    )

    (LAB / "notes.txt").write_text(
        "Windows security research exercise.\n"
    )

    print("[+] Laboratory initialized")


def encrypt():
    if not LAB.exists():
        print("[-] Initialize the lab first")
        return

    key = Fernet.generate_key()
    cipher = Fernet(key)

    KEY_FILE.write_bytes(key)

    for file in LAB.glob("*.txt"):
        if file == NOTE_FILE:
            continue

        encrypted = cipher.encrypt(file.read_bytes())
        file.with_suffix(file.suffix + ".locked").write_bytes(encrypted)

        print(f"[+] Simulated encryption: {file.name}")

    NOTE_FILE.write_text(
        "ASTRA SECURITY LAB\n"
        "==================\n"
        "This is a simulated ransomware exercise.\n"
        "Your test files have been encrypted.\n"
        "Use recovery.key with the restore command.\n"
    )

    print("[+] Simulation complete")


def decrypt():
    if not KEY_FILE.exists():
        print("[-] Recovery key missing")
        return

    cipher = Fernet(KEY_FILE.read_bytes())

    for file in LAB.glob("*.txt.locked"):
        encrypted = file.read_bytes()

        original = cipher.decrypt(encrypted)

        restored = file.with_suffix("")

        restored.write_bytes(original)

        file.unlink()

        print(f"[+] Restored: {restored.name}")

    print("[+] Recovery complete")


def main():
    parser = argparse.ArgumentParser(
        description="Contained Windows ransomware simulator"
    )

    parser.add_argument(
        "action",
        choices=["init", "encrypt", "restore"]
    )

    args = parser.parse_args()

    if args.action == "init":
        initialize()

    elif args.action == "encrypt":
        encrypt()

    elif args.action == "restore":
        decrypt()


if __name__ == "__main__":
    main()