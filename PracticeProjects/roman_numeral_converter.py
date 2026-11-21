# Convert numbers 1 through 3999 to Roman numerals and back.
# Practice: greedy algorithms, tuples, string scanning, and canonical validation.


NUMERALS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(number):
    if type(number) is not int or not 1 <= number <= 3999:
        raise ValueError("Number must be a whole number from 1 to 3999.")
    parts = []
    for value, symbol in NUMERALS:
        count, number = divmod(number, value)
        parts.append(symbol * count)
    return "".join(parts)


def from_roman(text):
    text = text.strip().upper()
    if not text or len(text) > 15 or any(symbol not in VALUES for symbol in text):
        raise ValueError("Enter a Roman numeral using I, V, X, L, C, D, and M.")
    total = 0
    for index, symbol in enumerate(text):
        value = VALUES[symbol]
        subtract = index + 1 < len(text) and value < VALUES[text[index + 1]]
        total += -value if subtract else value
    # A round trip rejects nonstandard forms such as IIII, IC, and VX.
    if not 1 <= total <= 3999 or to_roman(total) != text:
        raise ValueError("Use the standard Roman form for a number from 1 to 3999.")
    return total


def main():
    print("Roman Numeral Converter")
    while True:
        print("\n1. Number to Roman\n2. Roman to number\n3. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print(f"Roman: {to_roman(int(input('Whole number: ')))}")
            elif choice == "2":
                print(f"Number: {from_roman(input('Roman numeral: '))}")
            elif choice == "3":
                break
            else:
                print("Choose an option from 1 to 3.")
        except ValueError as error:
            print(f"Invalid numeral: {error}")


if __name__ == "__main__":
    main()
