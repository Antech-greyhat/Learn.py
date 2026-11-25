# Validate ISBN-10 and ISBN-13 or calculate a missing check digit.
# Practice: weighted sums, modular arithmetic, strings, and format validation.


def normalize(text):
    return "".join(text.split()).replace("-", "").upper()


def check_digit(prefix):
    prefix = normalize(prefix)
    if not prefix or any(character not in "0123456789" for character in prefix):
        raise ValueError("Prefix must contain ASCII digits only.")
    if len(prefix) == 9:
        remainder = (-sum((10 - index) * int(digit) for index, digit in enumerate(prefix))) % 11
        return "X" if remainder == 10 else str(remainder)
    if len(prefix) == 12 and prefix.startswith(("978", "979")):
        total = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(prefix))
        return str(-total % 10)
    raise ValueError("Use 9 digits for ISBN-10, or 12 digits starting with 978 or 979 for ISBN-13.")


def is_valid(text):
    text = normalize(text)
    if len(text) not in (10, 13):
        return False
    try:
        return check_digit(text[:-1]) == text[-1]
    except ValueError:
        return False


def main():
    print("ISBN Toolkit - ignores hyphens and whitespace; X is valid as an ISBN-10 check digit.")
    while True:
        print("\n1. Validate ISBN\n2. Calculate check digit\n3. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print("Valid ISBN." if is_valid(input("ISBN: ")) else "Invalid ISBN.")
            elif choice == "2":
                prefix = normalize(input("ISBN without its final digit: "))
                print(f"Complete ISBN: {prefix}{check_digit(prefix)}")
            elif choice == "3":
                break
            else:
                print("Choose an option from 1 to 3.")
        except ValueError as error:
            print(f"Invalid ISBN input: {error}")


if __name__ == "__main__":
    main()
