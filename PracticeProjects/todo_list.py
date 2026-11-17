# Add, complete, and remove tasks from a menu.
# Practice: lists, dictionaries, functions, enumerate, and exceptions.


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "pending"
        print(f"{number}. [{status}] {task['title']}")


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("The task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    print("Task added.")


def choose_task(tasks):
    if not tasks:
        print("No tasks to select.")
        return None

    show_tasks(tasks)
    try:
        index = int(input("Task number: ")) - 1
    except ValueError:
        print("Enter a whole number.")
        return None

    # Reject negative indexes so 0 cannot select the last task.
    if not 0 <= index < len(tasks):
        print("That task number does not exist.")
        return None
    return index


def main():
    tasks = []
    print("To-do List - tasks stay in memory until you exit.")

    while True:
        print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Remove task\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice in ("3", "4"):
            index = choose_task(tasks)
            if index is None:
                continue

            if choice == "3":
                tasks[index]["done"] = True
                print("Task marked complete.")
            else:
                removed_task = tasks.pop(index)
                print(f"Removed: {removed_task['title']}")
        elif choice == "5":
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    main()
