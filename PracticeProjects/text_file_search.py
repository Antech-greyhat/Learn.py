# Search a UTF-8 text file and print matching lines with line numbers.
# Practice: pathlib, generators, file handling, regular expressions, and exceptions.
from pathlib import Path
import re


def search_file(path, query, use_regex=False, case_sensitive=False):
    if not query:
        raise ValueError("Search query cannot be empty.")
    pattern = query if use_regex else re.escape(query)
    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        matcher = re.compile(pattern, flags)
    except re.error as error:
        raise ValueError(f"Invalid regular expression: {error}") from error
    # Yield one matching line at a time instead of reading the whole file.
    with Path(path).open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, start=1):
            if matcher.search(line):
                yield line_number, line.rstrip("\r\n")


def main():
    print("Text File Search - reads UTF-8 files without changing them.")
    while True:
        path = input("File path (q to quit): ").strip()
        if path.lower() == "q":
            break
        query = input("Search query: ")
        mode = input("Mode (1 = literal text, 2 = regular expression): ").strip()
        if mode not in ("1", "2"):
            print("Choose mode 1 or 2.")
            continue
        case_choice = input("Case-sensitive? (y/n): ").strip().lower()
        if case_choice not in ("y", "n"):
            print("Choose y or n.")
            continue
        try:
            matches = 0
            for line_number, line in search_file(path, query, mode == "2", case_choice == "y"):
                print(f"{line_number}: {line}")
                matches += 1
            print(f"Matching lines: {matches}")
        except (OSError, UnicodeError, ValueError) as error:
            print(f"Cannot search file: {error}")


if __name__ == "__main__":
    main()
