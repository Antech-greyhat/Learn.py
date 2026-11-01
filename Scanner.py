#!/usr/bin/env python3
"""
malware_scanner.py - a simple malware scanner in one file.
Uses only the Python standard library. Works on Windows, Linux and macOS.

What it does:
  1. Asks you for permission before it reads any file.
  2. Goes through the folder you choose and checks each file for:
       - known bad file hashes (SHA-256)
       - the EICAR antivirus test file
       - fake double extensions (e.g. invoice.pdf.exe)
       - programs hiding behind a document or picture extension
       - dangerous commands inside scripts (download-and-run, reverse shells,
         ransomware commands, crypto miners, web shells, Defender turned off)
       - packed or encrypted programs (high entropy)
  3. Uses ClamAV as well, if it is installed (much stronger detection).
  4. Saves a report. Moves files to quarantine ONLY if you say yes.

It never deletes files and never sends anything to the internet.

Usage:
    python scanner.py
    python scanner.py /path/to/folder
"""

import hashlib
import math
import os
import re
import shutil
import stat
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

#settings
MAX_HASH_SIZE = 200 * 1024 * 1024   # do not hash files bigger than 200 MB
CONTENT_LIMIT = 2 * 1024 * 1024     # only look inside the first 2 MB
CHUNK = 1024 * 1024
QUARANTINE_DIR = Path.home() / "malware_quarantine"

HIGH, MEDIUM, LOW = "HIGH", "MEDIUM", "LOW"
RANK = {HIGH: 3, MEDIUM: 2, LOW: 1}

# Folders that are not real files (Linux/macOS)
SKIP_PATHS = {"/proc", "/sys", "/dev", "/run", str(QUARANTINE_DIR)}

KNOWN_BAD_HASHES = {
    "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f": "EICAR test file",
}

# Built in two parts so that antivirus does not flag this script itself.
EICAR_MARK = b"EICAR-STANDARD-" + b"ANTIVIRUS-TEST-FILE"

SCRIPT_EXT = {".ps1", ".psm1", ".bat", ".cmd", ".vbs", ".vbe", ".js", ".jse",
              ".wsf", ".hta", ".sh", ".bash", ".py", ".php", ".pl", ".rb"}

DOC_EXT = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt",
           ".jpg", ".jpeg", ".png", ".gif", ".mp3", ".mp4"}

DOUBLE_EXT = re.compile(
    r"\.(pdf|docx?|xlsx?|pptx?|txt|jpe?g|png|gif|mp[34]|zip)"
    r"\.(exe|scr|com|pif|bat|cmd|vbs|js|jar|ps1|hta|lnk)$",
    re.IGNORECASE,
)

# (pattern, risk, plain explanation)
SUSPICIOUS_PATTERNS = [
    (rb"vssadmin[^\n]{0,40}delete\s+shadows", HIGH, "Deletes Windows backups (common in ransomware)"),
    (rb"wmic[^\n]{0,40}shadowcopy\s+delete", HIGH, "Deletes Windows backups (common in ransomware)"),
    (rb"bcdedit[^\n]{0,60}recoveryenabled\s+no", HIGH, "Turns off Windows recovery"),
    (rb"set-mppreference[^\n]{0,60}-disable", HIGH, "Turns off Windows Defender"),
    (rb"-e(nc|ncodedcommand)?\s+[A-Za-z0-9+/=]{60,}", HIGH, "Runs hidden (encoded) PowerShell"),
    (rb"mshta(\.exe)?\s+[\"']?https?://", HIGH, "Runs an HTA file from the internet"),
    (rb"/dev/tcp/\d{1,3}(\.\d{1,3}){3}/\d+", HIGH, "Reverse shell (gives someone remote control)"),
    (rb"\bnc(at)?\s[^\n]{0,60}-e\s+/bin/(ba)?sh", HIGH, "Reverse shell using netcat"),
    (rb"stratum\+tcp://", HIGH, "Crypto mining pool address"),
    (rb"eval\s*\(\s*\$_(POST|GET|REQUEST|COOKIE)", HIGH, "PHP web shell"),
    (rb"eval\s*\(\s*(base64_decode|gzinflate|str_rot13)\s*\(", HIGH, "Hidden PHP code"),
    (rb"exec\s*\(\s*(base64\.b64decode|zlib\.decompress|marshal\.loads)", HIGH, "Hidden Python code"),
    (rb"\bxmrig\b", MEDIUM, "Crypto miner name (XMRig)"),
    (rb"(curl|wget)\s[^\n|;]{0,150}\|\s*(sudo\s+)?(ba|z)?sh\b", MEDIUM, "Downloads a script and runs it at once"),
    (rb"certutil[^\n]{0,40}-urlcache", MEDIUM, "Uses certutil to download files"),
    (rb"bitsadmin[^\n]{0,40}/transfer", MEDIUM, "Uses bitsadmin to download files"),
    (rb"(downloadstring|downloadfile)\s*\(", MEDIUM, "Downloads content from the internet"),
    (rb"\b(iex|invoke-expression)\b", MEDIUM, "Runs code that is built while running"),
    (rb"reg(\.exe)?\s+add[^\n]{0,120}\\currentversion\\run", MEDIUM, "Adds itself to Windows startup"),
    (rb"wevtutil(\.exe)?\s+cl\b", MEDIUM, "Clears Windows event logs"),
    (rb"frombase64string", LOW, "Decodes Base64 data"),
    (rb"schtasks(\.exe)?\s[^\n]{0,40}/create", LOW, "Creates a scheduled task"),
    (rb"wscript\.shell", LOW, "Can run system commands (VBScript)"),
]
COMPILED = [(re.compile(p, re.IGNORECASE), risk, why) for p, risk, why in SUSPICIOUS_PATTERNS]

BANNER = r"""
==================================================
          SIMPLE MALWARE SCANNER (Python)
==================================================
"""


# helpers
def ask_yes_no(question):
    while True:
        try:
            answer = input(f"{question} [yes/no]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return False
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type yes or no.")


def get_permission():
    print(BANNER)
    print("This script will:")
    print("  - READ files in the folder you choose (it will not change them)")
    print("  - check them for signs of viruses and malware")
    print("  - save a report in the current folder")
    print("It will NOT delete files and will NOT send anything to the internet.")
    print("If it finds something, it will ask you again before moving any file.\n")
    return ask_yes_no("Do you give permission to scan your files?")


def choose_folder(cli_arg):
    if cli_arg:
        folder = Path(cli_arg).expanduser()
    else:
        default = Path.home()
        try:
            typed = input(f"Folder to scan (press Enter for {default}): ").strip().strip('"')
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        folder = Path(typed).expanduser() if typed else default
    folder = folder.resolve()
    if not folder.exists():
        print(f"[!] Not found: {folder}")
        return None
    return folder


def load_bad_hashes():
    hashes = dict(KNOWN_BAD_HASHES)
    extra = Path(__file__).resolve().parent / "bad_hashes.txt"
    if extra.exists():
        for line in extra.read_text(errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            h = line.split()[0].lower()
            if re.fullmatch(r"[0-9a-f]{64}", h):
                hashes[h] = "Hash listed in bad_hashes.txt"
        print(f"[+] Loaded {len(hashes)} bad hashes (including bad_hashes.txt)")
    return hashes


def iter_files(root):
    if root.is_file():
        yield root
        return
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = [d for d in dirnames if os.path.join(dirpath, d) not in SKIP_PATHS]
        for name in filenames:
            yield Path(dirpath) / name


def read_file(path, size):
    """Return (sha256 or None, first part of the file)."""
    with open(path, "rb") as f:
        if size > MAX_HASH_SIZE:
            return None, f.read(CONTENT_LIMIT)
        sha = hashlib.sha256()
        head = b""
        for chunk in iter(lambda: f.read(CHUNK), b""):
            sha.update(chunk)
            if len(head) < CONTENT_LIMIT:
                head += chunk[:CONTENT_LIMIT - len(head)]
        return sha.hexdigest(), head


def entropy(data):
    if not data:
        return 0.0
    n = len(data)
    return -sum(c / n * math.log2(c / n) for c in Counter(data).values())


def worst_risk(findings):
    return max(findings, key=lambda f: RANK[f[0]])[0]


#checks
def check_file(path, bad_hashes):
    findings = []
    info = os.lstat(path)
    if not stat.S_ISREG(info.st_mode):      # skip links, devices, pipes
        return findings
    size = info.st_size
    ext = path.suffix.lower()

    if DOUBLE_EXT.search(path.name):
        findings.append((HIGH, "Fake double extension (looks like a document but is a program)"))

    if size == 0:
        return findings

    sha, head = read_file(path, size)

    if sha and sha in bad_hashes:
        findings.append((HIGH, f"Known malware hash: {bad_hashes[sha]}"))
    elif EICAR_MARK in head[:256]:
        findings.append((HIGH, "EICAR antivirus test file"))

    is_program = head[:2] == b"MZ" or head[:4] == b"\x7fELF"
    if is_program and ext in DOC_EXT:
        findings.append((HIGH, "Program hiding behind a document/picture extension"))

    if ext in SCRIPT_EXT or head[:2] == b"#!":
        for rx, risk, why in COMPILED:
            if rx.search(head):
                findings.append((risk, why))

    if is_program and len(head) > 4096:
        e = entropy(head[:CHUNK])
        if e > 7.4:
            findings.append((LOW, f"Packed or encrypted program (entropy {e:.2f}). "
                                  "Many safe installers also look like this."))
    return findings


def run_clamav(root):
    exe = shutil.which("clamscan")
    if not exe:
        return []
    print(f"\n[+] Running ClamAV ({exe}). This can take a while...")
    try:
        proc = subprocess.run([exe, "-r", "-i", "--no-summary", str(root)],
                              capture_output=True, text=True, errors="ignore")
    except Exception as e:
        print(f"[!] ClamAV failed: {e}")
        return []
    hits = []
    for line in proc.stdout.splitlines():
        if line.endswith(" FOUND"):
            fpath, _, sig = line[:-len(" FOUND")].rpartition(": ")
            hits.append((fpath, sig))
    return hits


#output
def write_report(root, results, scanned, skipped, took):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report = Path.cwd() / f"scan_report_{stamp}.txt"
    lines = [
        "MALWARE SCAN REPORT",
        f"Date:          {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Scanned:       {root}",
        f"Files checked: {scanned}",
        f"Skipped:       {skipped} (no permission or could not open)",
        f"Time taken:    {took:.1f} seconds",
        "",
    ]
    if not results:
        lines.append("Nothing suspicious found.")
    for risk in (HIGH, MEDIUM, LOW):
        group = [(p, f) for p, f in results.items() if worst_risk(f) == risk]
        if not group:
            continue
        lines.append(f"===== {risk} RISK ({len(group)} files) =====")
        for p, f in group:
            lines.append(str(p))
            for r, why in f:
                lines.append(f"    - [{r}] {why}")
        lines.append("")
    lines.append("NOTE: A finding is a warning, not proof. Check each file before you act.")
    try:
        report.write_text("\n".join(lines), encoding="utf-8")
        return report
    except OSError as e:
        print(f"[!] Could not save report: {e}")
        return None


def quarantine(paths):
    QUARANTINE_DIR.mkdir(exist_ok=True)
    log = QUARANTINE_DIR / "quarantine_log.txt"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(log, "a", encoding="utf-8") as lf:
        for i, p in enumerate(paths, 1):
            target = QUARANTINE_DIR / f"{stamp}_{i}_{p.name}.quarantined"
            try:
                shutil.move(str(p), str(target))
                try:
                    os.chmod(target, 0o400)      # read-only, cannot run
                except OSError:
                    pass
                lf.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {p} -> {target}\n")
                print(f"  moved: {p}")
            except Exception as e:
                print(f"  [!] Could not move {p}: {e}")
    print(f"\nQuarantined files are in: {QUARANTINE_DIR}")
    print("To restore a file, move it back and remove '.quarantined' from its name.")
    print(f"The original locations are listed in: {log}")


#main
def main():
    if not get_permission():
        print("\nNo permission given. Nothing was scanned. Bye.")
        return 0

    root = choose_folder(sys.argv[1] if len(sys.argv) > 1 else None)
    if root is None:
        return 1

    bad_hashes = load_bad_hashes()
    use_clam = bool(shutil.which("clamscan")) and \
        ask_yes_no("ClamAV is installed. Use it as well (stronger but slower)?")

    me = Path(__file__).resolve()
    results, scanned, skipped = {}, 0, 0
    start = time.time()
    print(f"\n[+] Scanning {root}  (press Ctrl+C to stop)\n")

    try:
        for path in iter_files(root):
            if path.name == me.name and path.resolve() == me:
                continue
            try:
                found = check_file(path, bad_hashes)
            except OSError:
                skipped += 1
                continue
            scanned += 1
            if found:
                results[path] = found
                print(f"  [{worst_risk(found)}] {path}")
            if scanned % 1000 == 0:
                print(f"  ... {scanned} files checked")
    except KeyboardInterrupt:
        print("\n[!] Scan stopped. Showing what was found so far.")

    if use_clam:
        for fpath, sig in run_clamav(root):
            results.setdefault(Path(fpath), []).append((HIGH, f"ClamAV: {sig}"))
            print(f"  [HIGH] {fpath}  (ClamAV: {sig})")

    took = time.time() - start
    report = write_report(root, results, scanned, skipped, took)

    counts = Counter(worst_risk(f) for f in results.values())
    print("\n================ SUMMARY ================")
    print(f"Files checked : {scanned}")
    print(f"Skipped       : {skipped}")
    print(f"HIGH risk     : {counts.get(HIGH, 0)}")
    print(f"MEDIUM risk   : {counts.get(MEDIUM, 0)}")
    print(f"LOW risk      : {counts.get(LOW, 0)}")
    print(f"Time taken    : {took:.1f} seconds")
    if report:
        print(f"Report saved  : {report}")
    print("=========================================")

    high = [p for p, f in results.items() if worst_risk(f) == HIGH and p.exists()]
    if high:
        print("\nHIGH risk files:")
        for p in high:
            print(f"  - {p}")
        if ask_yes_no(f"\nDo you want to move these {len(high)} file(s) to quarantine?"):
            quarantine(high)
        else:
            print("OK. No files were moved.")
    elif not results:
        print("\nGood news: nothing suspicious found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
