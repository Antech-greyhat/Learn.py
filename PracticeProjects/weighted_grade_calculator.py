# Combine assessment scores using percentage weights that sum to exactly 100.
# Practice: Decimal, lists of dictionaries, validation, and weighted averages.
from decimal import Decimal, InvalidOperation, localcontext


def parse_percentage(text):
    if len(text) > 30:
        raise ValueError("Percentage input cannot exceed 30 characters.")
    try:
        value = Decimal(text.strip())
    except InvalidOperation as error:
        raise ValueError("Enter a numeric percentage.") from error
    if not value.is_finite() or not 0 <= value <= 100:
        raise ValueError("Percentage must be finite and from 0 to 100.")
    return value


def add_component(components, name, score_text, weight_text):
    name = name.strip()
    if not name or any(item["name"].casefold() == name.casefold() for item in components):
        raise ValueError("Assessment name must be nonempty and unique.")
    if len(components) >= 20:
        raise ValueError("Use at most 20 assessments.")
    score, weight = parse_percentage(score_text), parse_percentage(weight_text)
    with localcontext() as context:
        context.prec = 80
        if weight == 0 or sum(item["weight"] for item in components) + weight > 100:
            raise ValueError("Weight must be positive and total weights cannot exceed 100.")
    components.append({"name": name, "score": score, "weight": weight})


def calculate_grade(components):
    with localcontext() as context:
        context.prec = 80
        total_weight = sum(item["weight"] for item in components)
        if total_weight != 100:
            raise ValueError(f"Weights currently total {total_weight}; they must total 100.")
        return sum(item["score"] * item["weight"] for item in components) / 100


def main():
    components = []
    print("Weighted Grade Calculator - assessments last for this session.")
    while True:
        print("\n1. Add assessment\n2. View assessments\n3. Calculate grade\n4. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Assessment name: ")
                score = input("Score percentage: ")
                weight = input("Weight percentage: ")
                add_component(components, name, score, weight)
                print("Assessment added.")
            elif choice == "2":
                if not components:
                    print("No assessments yet.")
                for item in components:
                    print(f"{item['name']}: score {item['score']} | weight {item['weight']}%")
            elif choice == "3":
                print(f"Final grade: {calculate_grade(components):.2f}%")
            elif choice == "4":
                break
            else:
                print("Choose an option from 1 to 4.")
        except ValueError as error:
            print(f"Invalid grade input: {error}")


if __name__ == "__main__":
    main()
