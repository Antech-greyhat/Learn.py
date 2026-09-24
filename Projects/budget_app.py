class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = "{:.2f}".format(entry["amount"])[:7]
            items += f"{description:<23}{amount:>7}" + "\n"
        total = "Total: {:.2f}".format(self.get_balance())
        return title + items + total


def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        withdrawals.append(spent)
    total_spent = sum(withdrawals)
    percentages = [int((amt / total_spent) * 10) * 10 for amt in withdrawals]

    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "| "
        for percent in percentages:
            chart += "o  " if percent >= level else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_len = max(len(category.name) for category in categories)
    for i in range(max_name_len):
        chart += "     "
        for category in categories:
            chart += category.name[i] + "  " if i < len(category.name) else "   "
        if i != max_name_len - 1:
            chart += "\n"

    return chart