# Insert credit, buy snacks, and refund unused credit.
# Practice: classes, dictionaries, Decimal, state changes, and exceptions.
from decimal import Decimal, InvalidOperation


def parse_money(text):
    try:
        amount = Decimal(text)
        if not amount.is_finite() or not 0 < amount <= Decimal("1000000"):
            raise ValueError("Amount must be between 0.01 and 1000000.")
        if amount != amount.quantize(Decimal("0.01")):
            raise ValueError("Use at most two decimal places.")
    except InvalidOperation as error:
        raise ValueError("Enter a valid money amount.") from error
    return amount


class VendingMachine:
    def __init__(self):
        self.credit = Decimal("0.00")
        self.products = {
            "A1": {"name": "Water", "price": Decimal("1.00"), "stock": 3},
            "A2": {"name": "Juice", "price": Decimal("1.50"), "stock": 2},
            "B1": {"name": "Biscuits", "price": Decimal("0.75"), "stock": 4},
        }

    def insert_credit(self, text):
        amount = parse_money(text)
        if self.credit + amount > Decimal("1000000"):
            raise ValueError("Credit cannot exceed 1000000.")
        self.credit += amount

    def buy(self, code):
        code = code.strip().upper()
        if code not in self.products:
            raise ValueError("Product code not found.")
        product = self.products[code]
        if product["stock"] == 0:
            raise ValueError("Product is sold out.")
        if self.credit < product["price"]:
            raise ValueError("Insert more credit first.")
        # Validate first so a failed purchase cannot consume credit or stock.
        self.credit -= product["price"]
        product["stock"] -= 1
        return product["name"]

    def refund(self):
        amount = self.credit
        self.credit = Decimal("0.00")
        return amount

    def show_products(self):
        for code, product in self.products.items():
            print(f"{code}: {product['name']} | {product['price']:.2f} | Stock: {product['stock']}")
        print(f"Credit: {self.credit:.2f}")


def main():
    machine = VendingMachine()
    print("Vending Machine - simulated money; stock lasts for this session.")
    while True:
        print("\n1. View products\n2. Insert credit\n3. Buy\n4. Refund\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                machine.show_products()
            elif choice == "2":
                machine.insert_credit(input("Amount: ").strip())
                print(f"Credit: {machine.credit:.2f}")
            elif choice == "3":
                print(f"Enjoy your {machine.buy(input('Product code: '))}!")
                print(f"Credit: {machine.credit:.2f}")
            elif choice == "4":
                print(f"Refund: {machine.refund():.2f}")
            elif choice == "5":
                print(f"Refund: {machine.refund():.2f}")
                break
            else:
                print("Choose an option from 1 to 5.")
        except ValueError as error:
            print(f"Transaction unchanged: {error}")


if __name__ == "__main__":
    main()
