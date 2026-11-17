# Convert length, mass, and temperature from a menu.
# Practice: dictionaries, tuples, functions, arithmetic, and exceptions.
import math


CONVERSIONS = {
    "1": ("kilometres", "miles", lambda value: value / 1.609344),
    "2": ("miles", "kilometres", lambda value: value * 1.609344),
    "3": ("kilograms", "pounds", lambda value: value / 0.45359237),
    "4": ("pounds", "kilograms", lambda value: value * 0.45359237),
    "5": ("Celsius", "Fahrenheit", lambda value: value * 9 / 5 + 32),
    "6": ("Fahrenheit", "Celsius", lambda value: (value - 32) * 5 / 9),
}


def convert_value(choice, value):
    if choice not in CONVERSIONS:
        raise ValueError("Choose a conversion from 1 to 6.")
    if not math.isfinite(value):
        raise ValueError("Value must be a finite number.")
    if choice in ("1", "2", "3", "4") and value < 0:
        raise ValueError("Length and mass cannot be negative.")

    source_unit, target_unit, converter = CONVERSIONS[choice]
    result = converter(value)
    if not math.isfinite(result):
        raise ValueError("Value is too large to convert.")
    return source_unit, target_unit, result


def main():
    print("Unit Converter")
    while True:
        for choice, (source_unit, target_unit, converter) in CONVERSIONS.items():
            print(f"{choice}. {source_unit} to {target_unit}")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "7":
            break
        if choice not in CONVERSIONS:
            print("Choose an option from 1 to 7.")
            continue

        try:
            value = float(input("Value: "))
            source_unit, target_unit, result = convert_value(choice, value)
            print(f"{value:g} {source_unit} = {result:.4f} {target_unit}\n")
        except ValueError as error:
            print(f"Conversion failed: {error}\n")


if __name__ == "__main__":
    main()
