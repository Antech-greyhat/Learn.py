#!/usr/bin/env python3
"""
Scan a Git repository's full history for exposed tokens/secrets.

Usage:
    python git_scan.py /path/to/repo
    python git_scan.py .          # current directory
"""

import subprocess
import re
import sys
import os

# Common secret patterns. Extend as needed.
PATTERNS = {
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Access Key": r"(?i)aws_secret_access_key\s*[:=]\s*['\"][A-Za-z0-9/+=]{40}['\"]",
    "GitHub Token": r"gh[pousr]_[A-Za-z0-9_]{36,255}",
    "GitHub Fine-grained PAT": r"github_pat_[A-Za-z0-9_]{82}",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9-]{10,}",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Stripe Key": r"(?:sk|pk)_(?:live|test)_[0-9a-zA-Z]{24,}",
    "Private Key": r"-----BEGIN (?:RSA|DSA|EC|OPENSSH|PGP) PRIVATE KEY-----",
    "JWT": r"eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+",
    "Generic Secret": r"(?i)(?:secret|token|password|passwd|pwd|api[_-]?key|apikey)\s*[:=]\s*['\"][^'\"]{8,}['\"]",
}

def scan_repo(repo_path: str):
    if not os.path.isdir(repo_path):
        print(f"Error: {repo_path} is not a directory")
        sys.exit(1)

    cmd = ["git", "-C", repo_path, "log", "-p", "--all", "--full-history"]
    try:
        output = subprocess.check_output(
            cmd, stderr=subprocess.DEVNULL, text=True, errors="replace"
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running git: {e}")
        sys.exit(1)

    current_commit = None
    current_file = None
    findings = 0

    for line in output.splitlines():
        if line.startswith("commit "):
            current_commit = line.split()[1]
        elif line.startswith("+++ b/"):
            current_file = line[6:]
        elif line.startswith("+") and not line.startswith("+++"):
            added_line = line[1:]
            for name, pattern in PATTERNS.items():
                for match in re.finditer(pattern, added_line):
                    findings += 1
                    print(f"[{name}]")
                    print(f"  Commit : {current_commit[:12] if current_commit else '?'}")
                    print(f"  File   : {current_file or '?'}")
                    print(f"  Match  : {match.group(0)[:80]}{'...' if len(match.group(0)) > 80 else ''}")
                    print(f"  Line   : {added_line.strip()[:200]}")
                    print("-" * 60)

    if findings == 0:
        print("No obvious secrets found in history.")
    else:
        print(f"\nTotal potential secrets found: {findings}")
        print("Rotate/revoke any live credentials immediately.")

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_repo(repo)