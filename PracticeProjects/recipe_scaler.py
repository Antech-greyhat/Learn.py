# Scale a pancake recipe without losing fractional quantities.
# Practice: Fraction, dictionaries, tuples, comprehensions, and exceptions.
from fractions import Fraction


BASE_SERVINGS = 4
PANCAKES = {
    "flour": (Fraction(2), "cups"),
    "milk": (Fraction(3, 2), "cups"),
    "eggs": (Fraction(2), "eggs"),
    "baking powder": (Fraction(2), "teaspoons"),
}


def scale_recipe(recipe, original_servings, target_servings):
    if (type(original_servings) is not int or type(target_servings) is not int
            or original_servings <= 0 or target_servings <= 0):
        raise ValueError("Servings must be positive whole numbers.")
    factor = Fraction(target_servings, original_servings)
    return {name: (quantity * factor, unit)
            for name, (quantity, unit) in recipe.items()}


def add_ingredient(recipe, name, quantity_text, unit):
    name = name.strip().lower()
    unit = unit.strip()
    if not name or not unit:
        raise ValueError("Ingredient name and unit cannot be empty.")
    if name in recipe:
        raise ValueError("Ingredient already exists.")
    try:
        quantity = Fraction(quantity_text)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError("Enter a number or fraction such as 1.5 or 3/2.") from error
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    recipe[name] = (quantity, unit)


def show_recipe(recipe, servings):
    print(f"\nRecipe for {servings} serving(s):")
    for name, (quantity, unit) in recipe.items():
        print(f"{name}: {quantity} {unit}")
    print("Fractional eggs can be beaten and measured before adding.")


def main():
    recipe = dict(PANCAKES)
    print("Recipe Scaler - additions last for this session.")
    print(f"The base pancake recipe makes {BASE_SERVINGS} servings.")
    while True:
        print("\n1. View base recipe\n2. Scale recipe\n3. Add base ingredient\n4. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                show_recipe(recipe, BASE_SERVINGS)
            elif choice == "2":
                servings = int(input("Target servings: "))
                show_recipe(scale_recipe(recipe, BASE_SERVINGS, servings), servings)
            elif choice == "3":
                name = input("Ingredient name: ")
                quantity = input(f"Quantity for {BASE_SERVINGS} servings: ").strip()
                unit = input("Unit: ")
                add_ingredient(recipe, name, quantity, unit)
                print("Ingredient added to the base recipe.")
            elif choice == "4":
                break
            else:
                print("Choose an option from 1 to 4.")
        except ValueError as error:
            print(f"Invalid recipe input: {error}")


if __name__ == "__main__":
    main()
