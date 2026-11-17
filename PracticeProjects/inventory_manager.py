# Add products, restock them, and sell available stock.
# Practice: classes, methods, dictionaries, validation, and exceptions.
import math


class Product:
    def __init__(self, name, price, quantity):
        name = name.strip()
        if not name:
            raise ValueError("The product name cannot be empty.")
        if not math.isfinite(price) or price <= 0:
            raise ValueError("The price must be a positive, finite number.")
        if quantity < 0:
            raise ValueError("Starting stock cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, quantity):
        if quantity <= 0:
            raise ValueError("The quantity must be positive.")
        self.quantity += quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("The quantity must be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock.")

        self.quantity -= quantity
        return self.price * quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} in stock, {self.price:.2f} each"


def add_product(inventory):
    name = input("Product name: ").strip()
    if not name:
        print("The product name cannot be empty.")
        return

    # Lowercase keys make product lookup ignore letter case.
    key = name.lower()
    if key in inventory:
        print("That product already exists. Use the restock option.")
        return

    try:
        price = float(input("Price per item: "))
        quantity = int(input("Starting stock: "))
        inventory[key] = Product(name, price, quantity)
    except ValueError as error:
        print(f"Product not added: {error}")
        return

    print("Product added.")


def show_inventory(inventory):
    if not inventory:
        print("No products yet.")
        return

    for key in sorted(inventory):
        print(inventory[key])

    total_value = sum(product.price * product.quantity for product in inventory.values())
    print(f"Stock value: {total_value:.2f}")


def change_stock(inventory, action):
    if not inventory:
        print("Add a product first.")
        return

    key = input("Product name: ").strip().lower()
    product = inventory.get(key)
    if product is None:
        print("Product not found.")
        return

    try:
        quantity = int(input("Quantity: "))
        if action == "restock":
            product.restock(quantity)
            print(f"Stock is now {product.quantity}.")
        else:
            sale_total = product.sell(quantity)
            print(f"Sale total: {sale_total:.2f}. Stock left: {product.quantity}.")
    except ValueError as error:
        print(f"Stock unchanged: {error}")


def main():
    inventory = {}
    print("Inventory Manager - stock stays in memory until you exit.")

    while True:
        print("\n1. Add product\n2. View stock\n3. Restock\n4. Sell\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            show_inventory(inventory)
        elif choice == "3":
            change_stock(inventory, "restock")
        elif choice == "4":
            change_stock(inventory, "sell")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
