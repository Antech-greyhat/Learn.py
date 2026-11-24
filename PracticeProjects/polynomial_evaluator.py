# Evaluate a polynomial efficiently using Horner's method.
# Practice: coefficient lists, loops, finite numbers, and numeric algorithms.
import math


def evaluate_polynomial(coefficients, x):
    if not coefficients or len(coefficients) > 100:
        raise ValueError("Enter from 1 to 100 coefficients.")
    if not math.isfinite(x) or any(not math.isfinite(value) for value in coefficients):
        raise ValueError("Coefficients and x must be finite numbers.")
    result = 0.0
    for coefficient in coefficients:
        # For [a, b, c], this computes (a*x + b)*x + c.
        result = result * x + coefficient
        if not math.isfinite(result):
            raise ValueError("Result is too large to represent.")
    return result


def derivative_coefficients(coefficients):
    degree = len(coefficients) - 1
    return [coefficient * (degree - index) for index, coefficient in enumerate(coefficients[:-1])] or [0]


def main():
    print("Polynomial Evaluator - enter coefficients from highest power to constant.")
    print("Example: 2,3,4 represents 2*x^2 + 3*x + 4.")
    while True:
        text = input("Comma-separated coefficients (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            coefficients = [float(part) for part in text.split(",")]
            x = float(input("Value of x: "))
            value = evaluate_polynomial(coefficients, x)
            slope = evaluate_polynomial(derivative_coefficients(coefficients), x)
            print(f"P(x): {value:g} | P'(x): {slope:g}")
        except (ValueError, OverflowError) as error:
            print(f"Invalid polynomial: {error}")


if __name__ == "__main__":
    main()
