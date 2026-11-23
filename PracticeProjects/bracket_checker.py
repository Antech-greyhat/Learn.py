# Check the nesting of (), [], and {} and report the first mismatch.
# Practice: stacks, dictionaries, enumeration, and early returns.


PAIRS = {")": "(", "]": "[", "}": "{"}


def check_brackets(text):
    stack = []
    for position, character in enumerate(text, 1):
        if character in PAIRS.values():
            stack.append((character, position))
        elif character in PAIRS:
            if not stack:
                return False, f"Unexpected {character} at position {position}."
            opening, opened_at = stack[-1]
            if opening != PAIRS[character]:
                return False, f"{character} at position {position} does not match {opening} at {opened_at}."
            stack.pop()
    if stack:
        opening, position = stack[-1]
        return False, f"Unclosed {opening} at position {position}."
    return True, "All brackets are balanced."


def main():
    print("Bracket Checker - checks all brackets, including those inside quoted text.")
    while True:
        text = input("Text to check (q to quit): ")
        if text.strip().lower() == "q":
            break
        balanced, message = check_brackets(text)
        print(f"{'Valid' if balanced else 'Invalid'}: {message}")


if __name__ == "__main__":
    main()
