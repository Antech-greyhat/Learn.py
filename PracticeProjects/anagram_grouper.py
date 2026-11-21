# Group words or phrases with the same letters, ignoring case and punctuation.
# Practice: Unicode normalization, dictionaries, sorted strings, and grouping.
import unicodedata


def signature(text):
    normalized = unicodedata.normalize("NFC", text.casefold())
    letters = [character for character in normalized if character.isalpha()]
    if not letters:
        raise ValueError("Each entry must contain at least one letter.")
    return "".join(sorted(letters))


def group_anagrams(entries):
    groups = {}
    seen = set()
    for entry in entries:
        entry = entry.strip()
        key = signature(entry)
        # Keep the first spelling of duplicate entries.
        identity = unicodedata.normalize("NFC", entry.casefold())
        if identity not in seen:
            groups.setdefault(key, []).append(entry)
            seen.add(identity)
    return list(groups.values())


def main():
    print("Anagram Grouper - accents are preserved; punctuation and case are ignored.")
    while True:
        text = input("Comma-separated words or phrases (q to quit): ")
        if text.strip().lower() == "q":
            break
        try:
            for number, group in enumerate(group_anagrams(text.split(",")), 1):
                print(f"Group {number}: {' | '.join(group)}")
        except ValueError as error:
            print(f"Invalid entries: {error}")


if __name__ == "__main__":
    main()
