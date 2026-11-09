
#!/usr/bin/env python3

"""
Automated GitHub Pull Request Assistance 
"""

import argparse
import subprocess
import sys


class PRShark:

    def __init__(self, base="main"):
        self.base = base
        self.branch = self.git("branch", "--show-current")

    @staticmethod
    def run(command, check=True):
        result = subprocess.run(
            command,
            text=True,
            capture_output=True
        )

        if check and result.returncode != 0:
            raise RuntimeError(
                result.stderr.strip() or "Command failed"
            )

        return result

    def git(self, *args, check=True):
        return self.run(["git", *args], check).stdout.strip()

    def validate(self):
        if not self.git("rev-parse", "--is-inside-work-tree"):
            raise RuntimeError("Not inside a Git repository.")

        if self.branch in ("main", "master", self.base):
            raise RuntimeError(
                "Create a feature branch before opening a PR."
            )

        self.run(["gh", "auth", "status"])

        print(f"[+] Repository branch: {self.branch}")
        print(f"[+] Target branch: {self.base}")

    def commit_changes(self, message, coauthor=None):
        staged = self.run(
            ["git", "diff", "--cached", "--quiet"],
            check=False
        )

        if staged.returncode == 0:
            if coauthor:
                raise RuntimeError(
                    "Co-author attribution requires a new "
                    "commit containing genuine joint work."
                )
            print("[*] No staged changes. Using existing commits.")
            return

        if staged.returncode != 1:
            raise RuntimeError("Could not inspect staged changes.")

        if coauthor:
            name, email = coauthor

            if not name.strip() or not email.strip():
                raise RuntimeError("Invalid co-author details.")

            confirmation = input(
                f"Confirm {name} genuinely contributed "
                "to these changes? [y/N]: "
            ).lower()

            if confirmation != "y":
                raise RuntimeError("Co-author attribution cancelled.")

            message += (
                f"\n\nCo-authored-by: {name} <{email}>"
            )

        self.git("commit", "-m", message)
        print("[+] Commit created.")

    def push(self):
        self.git(
            "push",
            "--set-upstream",
            "origin",
            self.branch
        )
        print("[+] Branch pushed successfully.")

    def create_pr(self, title, body):
        existing = self.run([
            "gh", "pr", "view",
            self.branch,
            "--json", "url"
        ], check=False)

        if existing.returncode == 0:
            print("[!] A PR already exists:")
            print(existing.stdout)
            return

        self.run([
            "gh", "pr", "create",
            "--base", self.base,
            "--head", self.branch,
            "--title", title,
            "--body", body
        ])

        print("[+] Pull request created successfully!")

    def execute(
        self,
        title,
        body,
        message,
        coauthor=None
    ):
        try:
            self.validate()

            self.git("fetch", "origin", self.base)

            self.commit_changes(message, coauthor)

            # Ensure there are actual commits to submit.
            ahead = self.git(
                "rev-list",
                "--count",
                f"origin/{self.base}..HEAD"
            )

            if int(ahead) < 1:
                raise RuntimeError(
                    "No commits ahead of the target branch."
                )

            self.push()
            self.create_pr(title, body)

            print("\n[PRShark] Workflow completed.")

        except Exception as error:
            print(f"\n[ERROR] {error}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Automate GitHub pull request creation."
    )

    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--commit", default="feat: contribution")
    parser.add_argument("--base", default="main")

    parser.add_argument(
        "--co-author-name",
        help="Name of genuine co-author"
    )

    parser.add_argument(
        "--co-author-email",
        help="GitHub-associated email of co-author"
    )

    args = parser.parse_args()

    if bool(args.co_author_name) != bool(args.co_author_email):
        parser.error(
            "Provide both co-author name and email."
        )

    coauthor = None

    if args.co_author_name:
        coauthor = (
            args.co_author_name,
            args.co_author_email
        )

    shark = PRShark(base=args.base)

    shark.execute(
        title=args.title,
        body=args.body,
        message=args.commit,
        coauthor=coauthor
    )


if __name__ == "__main__":
    main()
