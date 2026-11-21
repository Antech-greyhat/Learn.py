# Convert signed whole numbers between bases 2 through 36.
# Practice: divmod, digit lookup, loops, place values, and validation.


DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def validate_base(base):
    if type(base) is not int or not 2 <= base <= 36:
        raise ValueError("Base must be a whole number from 2 to 36.")


def parse_number(text, base):
    validate_base(base)
    text = text.strip().upper()
    sign = -1 if text.startswith("-") else 1
    if text.startswith(("-", "+")):
        text = text[1:]
    if not text or len(text) > 200:
        raise ValueError("Enter from 1 to 200 digits, with an optional sign.")
    value = 0
    for character in text:
        if character not in DIGITS[:base]:
            raise ValueError(f"Digit {character!r} is not valid in base {base}.")
        value = value * base + DIGITS.index(character)
    return sign * value


def format_number(value, base):
    validate_base(base)
    if type(value) is not int:
        raise ValueError("Value must be a whole number.")
    if value == 0:
        return "0"
    remaining = abs(value)
    digits = []
    while remaining:
        remaining, remainder = divmod(remaining, base)
        digits.append(DIGITS[remainder])
    return ("-" if value < 0 else "") + "".join(reversed(digits))


def main():
    print("Base Converter - use plain digits without prefixes such as 0x.")
    while True:
        text = input("Number (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            source = int(input("Source base (2-36): "))
            target = int(input("Target base (2-36): "))
            value = parse_number(text, source)
            print(f"Converted: {format_number(value, target)}")
        except ValueError as error:
            print(f"Invalid conversion: {error}")


if __name__ == "__main__":
    main()
