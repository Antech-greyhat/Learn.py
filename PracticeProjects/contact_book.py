# Add, search, update, and delete contacts from a menu.
# Practice: dictionaries, strings, functions, and loops.


def add_contact(contacts):
    name = input("Name: ").strip()
    key = name.lower()
    if not name:
        print("Name cannot be empty.")
        return
    if key in contacts:
        print("Contact already exists. Use the update option.")
        return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    if not phone or not email:
        print("Phone and email cannot be empty.")
        return

    contacts[key] = {"name": name, "phone": phone, "email": email}
    print("Contact added.")


def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for key in sorted(contacts):
        contact = contacts[key]
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def search_contacts(contacts):
    query = input("Search name: ").strip().lower()
    if not query:
        print("Search text cannot be empty.")
        return

    matches = {key: contact for key, contact in contacts.items() if query in key}
    show_contacts(matches)


def update_contact(contacts):
    key = input("Contact name: ").strip().lower()
    if key not in contacts:
        print("Contact not found.")
        return

    contact = contacts[key]
    # Blank input keeps the current value.
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    contact["phone"] = phone or contact["phone"]
    contact["email"] = email or contact["email"]
    print("Contact updated.")


def delete_contact(contacts):
    key = input("Contact name: ").strip().lower()
    removed = contacts.pop(key, None)
    if removed is None:
        print("Contact not found.")
    else:
        print(f"Deleted: {removed['name']}")


def main():
    contacts = {}
    print("Contact Book - contacts stay in memory until you exit.")

    while True:
        print("\n1. Add\n2. View all\n3. Search\n4. Update\n5. Delete\n6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Choose an option from 1 to 6.")


if __name__ == "__main__":
    main()
