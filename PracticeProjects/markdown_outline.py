# Extract ATX headings from Markdown while skipping fenced code blocks.
# Practice: regular expressions, generators, file handling, and state machines.
from pathlib import Path
import re


HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def extract_headings(lines):
    fence_character = None
    fence_length = 0
    for line_number, line in enumerate(lines, 1):
        line = line.rstrip("\r\n")
        if fence_character is not None:
            closing = re.fullmatch(r" {0,3}" + re.escape(fence_character) + "{" + str(fence_length) + r",}[ \t]*", line)
            if closing:
                fence_character = None
            continue
        fence = FENCE.match(line)
        if fence:
            marker, info = fence.groups()
            # Backtick info strings cannot themselves contain backticks.
            if marker[0] == "~" or "`" not in info:
                fence_character, fence_length = marker[0], len(marker)
                continue
        heading = HEADING.match(line)
        if heading:
            markers, title = heading.groups()
            title = re.sub(r"(?:^|[ \t]+)#+[ \t]*$", "", title or "").strip()
            yield line_number, len(markers), title


def outline_file(path):
    with Path(path).open(encoding="utf-8-sig") as source:
        yield from extract_headings(source)


def main():
    print("Markdown Outline - ATX # headings; skips fenced code blocks.")
    print("Setext headings, HTML blocks, and nested blockquotes are outside this exercise.")
    while True:
        path = input("Markdown path (q to quit): ").strip()
        if path.lower() == "q":
            break
        try:
            count = 0
            for line_number, level, title in outline_file(path):
                print(f"{'  ' * (level - 1)}{title or '(empty heading)'} (line {line_number})")
                count += 1
            print(f"Headings: {count}")
        except (OSError, UnicodeError) as error:
            print(f"Cannot read outline: {error}")


if __name__ == "__main__":
    main()
