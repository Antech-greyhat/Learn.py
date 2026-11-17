# Record expenses and summarize spending by category.
# Practice: lists, dictionaries, functions, sorting, and exceptions.
import math


def add_expense(expenses):
    category = input("Category: ").strip().lower()
    description = input("Description: ").strip()
    if not category or not description:
        print("Category and description cannot be empty.")
        return

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Enter a valid amount.")
        return

    # Reject infinity and NaN as well as nonpositive amounts.
    if not math.isfinite(amount) or amount <= 0:
        print("The amount must be a positive, finite number.")
        return

    expenses.append({"category": category, "description": description, "amount": amount})
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} "
            f"({expense['category']}): {expense['amount']:.2f}"
        )


def show_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("Spending by category:")
    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")

    print(f"Total spent: {sum(totals.values()):.2f}")
    largest = max(expenses, key=lambda expense: expense["amount"])
    print(f"Largest expense: {largest['description']} ({largest['amount']:.2f})")


def main():
    expenses = []
    print("Expense Tracker - expenses stay in memory until you exit.")

    while True:
        print("\n1. Add expense\n2. View expenses\n3. Category totals\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            break
        else:
            print("Choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
