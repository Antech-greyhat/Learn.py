# Build a shopping cart and print a receipt with a discount.
# Practice: lists, dictionaries, arithmetic, functions, and exceptions.
import math


def add_item(cart):
    name = input("Item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    try:
        price = float(input("Price per item: "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Enter a numeric price and a whole-number quantity.")
        return

    if not math.isfinite(price) or price <= 0 or quantity <= 0:
        print("Price and quantity must be positive; price must be finite.")
        return

    cart.append({"name": name, "price": price, "quantity": quantity})
    print("Item added.")


def show_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    for number, item in enumerate(cart, start=1):
        line_total = item["price"] * item["quantity"]
        print(f"{number}. {item['name']} x {item['quantity']} @ {item['price']:.2f} = {line_total:.2f}")


def remove_item(cart):
    if not cart:
        print("Cart is empty.")
        return

    show_cart(cart)
    try:
        index = int(input("Item number: ")) - 1
    except ValueError:
        print("Enter a whole number.")
        return
    if not 0 <= index < len(cart):
        print("Item number does not exist.")
        return

    item = cart.pop(index)
    print(f"Removed: {item['name']}")


def print_receipt(cart):
    if not cart:
        print("Cart is empty.")
        return

    try:
        discount = float(input("Discount percentage (0-100): "))
    except ValueError:
        print("Enter a valid percentage.")
        return
    if not math.isfinite(discount) or not 0 <= discount <= 100:
        print("Discount must be from 0 to 100.")
        return

    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    saving = subtotal * (discount / 100)
    show_cart(cart)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {saving:.2f} ({discount:g}%)")
    print(f"Total due: {subtotal - saving:.2f}")


def main():
    cart = []
    print("Shopping Receipt - cart stays in memory until you exit.")

    while True:
        print("\n1. Add item\n2. View cart\n3. Remove item\n4. Print receipt\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item(cart)
        elif choice == "2":
            show_cart(cart)
        elif choice == "3":
            remove_item(cart)
        elif choice == "4":
            print_receipt(cart)
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
