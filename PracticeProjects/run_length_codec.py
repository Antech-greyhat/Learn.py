# Encode repeated characters and decode them back into text.
# Practice: strings, lists, tuples, JSON, validation, and loops.
import json


MAX_TEXT_LENGTH = 10000


def encode(text):
    if len(text) > MAX_TEXT_LENGTH:
        raise ValueError(f"Text cannot exceed {MAX_TEXT_LENGTH} characters.")
    runs = []
    for character in text:
        if runs and runs[-1][0] == character:
            runs[-1][1] += 1
        else:
            runs.append([character, 1])
    return runs


def decode(runs):
    if not isinstance(runs, list):
        raise ValueError("Encoded data must be a JSON list of [character, count] pairs.")
    parts = []
    total = 0
    for run in runs:
        if not isinstance(run, list) or len(run) != 2:
            raise ValueError("Each run must contain a character and a count.")
        character, count = run
        if not isinstance(character, str) or len(character) != 1:
            raise ValueError("Each character must be a string of length one.")
        if type(count) is not int or count <= 0:
            raise ValueError("Counts must be positive whole numbers.")
        total += count
        if total > MAX_TEXT_LENGTH:
            raise ValueError(f"Decoded text cannot exceed {MAX_TEXT_LENGTH} characters.")
        parts.append(character * count)
    return "".join(parts)


def main():
    print("Run Length Codec - JSON pairs preserve digits, spaces, and Unicode.")
    print("This format demonstrates encoding; it may be larger than the original.")
    while True:
        print("\n1. Encode text\n2. Decode JSON\n3. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                # Do not strip: leading and trailing spaces are part of the data.
                text = input("Text: ")
                print(json.dumps(encode(text), ensure_ascii=False))
            elif choice == "2":
                text = input('JSON pairs, such as [["a", 3], ["b", 1]]: ')
                print(f"Decoded: {decode(json.loads(text))}")
            elif choice == "3":
                break
            else:
                print("Choose an option from 1 to 3.")
        except (ValueError, RecursionError) as error:
            print(f"Invalid codec input: {error}")


if __name__ == "__main__":
    main()
