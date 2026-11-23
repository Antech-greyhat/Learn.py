# Calculate with fractions and display an exact simplified result.
# Practice: Fraction, operator dispatch, dictionaries, and exceptions.
from fractions import Fraction
import operator


OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def calculate(left_text, symbol, right_text):
    if symbol not in OPERATIONS:
        raise ValueError("Choose +, -, *, or /.")
    if max(len(left_text), len(right_text)) > 200:
        raise ValueError("Each number must be at most 200 characters.")
    try:
        left = Fraction(left_text.strip())
        right = Fraction(right_text.strip())
        return OPERATIONS[symbol](left, right)
    except ZeroDivisionError as error:
        raise ValueError("Denominators and divisors cannot be zero.") from error
    except ValueError as error:
        raise ValueError("Enter fractions or decimal numbers, such as 1/2 or 0.25.") from error


def main():
    print("Fraction Calculator - exact answers with reduced denominators.")
    while True:
        left = input("First number (q to quit): ").strip()
        if left.lower() == "q":
            break
        symbol = input("Operation (+ - * /): ").strip()
        right = input("Second number: ").strip()
        try:
            result = calculate(left, symbol, right)
            print(f"Result: {result} | Numerator: {result.numerator} | Denominator: {result.denominator}")
        except ValueError as error:
            print(f"Invalid calculation: {error}")


if __name__ == "__main__":
    main()
