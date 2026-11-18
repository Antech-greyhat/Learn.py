# Deposit or withdraw savings and track progress toward a goal.
# Practice: classes, methods, arithmetic, loops, and exceptions.
import math


class SavingsGoal:
    def __init__(self, name, target):
        if not name.strip():
            raise ValueError("Goal name cannot be empty.")
        if not math.isfinite(target) or target <= 0:
            raise ValueError("Target must be a positive, finite number.")
        self.name = name.strip()
        self.target = target
        self.balance = 0

    def deposit(self, amount):
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("Amount must be a positive, finite number.")
        if not math.isfinite(self.balance + amount):
            raise ValueError("Amount is too large.")
        self.balance += amount

    def withdraw(self, amount):
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("Amount must be a positive, finite number.")
        if amount > self.balance:
            raise ValueError("Not enough savings.")
        self.balance -= amount

    def show_progress(self):
        percentage = self.balance / self.target * 100
        remaining = max(self.target - self.balance, 0)
        print(f"{self.name}: {self.balance:.2f} saved of {self.target:.2f}")
        print(f"Progress: {percentage:.1f}% | Remaining: {remaining:.2f}")
        if self.balance >= self.target:
            print("Goal reached!")


def main():
    print("Savings Goal Tracker - savings stay in memory until you exit.")
    while True:
        name = input("Goal name: ").strip()
        try:
            target = float(input("Target amount: "))
            goal = SavingsGoal(name, target)
            break
        except ValueError as error:
            print(f"Invalid goal: {error}")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View progress\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice in ("1", "2"):
            try:
                amount = float(input("Amount: "))
                if choice == "1":
                    goal.deposit(amount)
                else:
                    goal.withdraw(amount)
                goal.show_progress()
            except ValueError as error:
                print(f"Savings unchanged: {error}")
        elif choice == "3":
            goal.show_progress()
        elif choice == "4":
            break
        else:
            print("Choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
