# Record habit completion dates and count daily streaks.
# Practice: dictionaries, sets, dates, loops, and exceptions.
from datetime import date, timedelta


def add_habit(habits):
    name = input("Habit name: ").strip()
    key = name.lower()
    if not name:
        print("Habit name cannot be empty.")
        return
    if key in habits:
        print("Habit already exists.")
        return

    habits[key] = {"name": name, "dates": set()}
    print("Habit added.")


def mark_complete(habits):
    key = input("Habit name: ").strip().lower()
    if key not in habits:
        print("Habit not found.")
        return

    text = input("Completion date YYYY-MM-DD (blank for today): ").strip()
    try:
        completed_on = date.fromisoformat(text) if text else date.today()
    except ValueError:
        print("Enter a valid date in YYYY-MM-DD format.")
        return
    if completed_on > date.today():
        print("Completion date cannot be in the future.")
        return

    completed_dates = habits[key]["dates"]
    if completed_on in completed_dates:
        print("Habit is already complete on that date.")
        return
    completed_dates.add(completed_on)
    print(f"Completion recorded for {completed_on}.")


def get_streak(completed_dates, ending_on):
    streak = 0
    current_day = ending_on
    while current_day in completed_dates:
        streak += 1
        current_day -= timedelta(days=1)
    return streak


def show_habits(habits):
    if not habits:
        print("No habits yet.")
        return

    today = date.today()
    for key in sorted(habits):
        habit = habits[key]
        status = "done" if today in habit["dates"] else "pending"
        streak = get_streak(habit["dates"], today)
        print(f"{habit['name']}: {status} | Completed days: {len(habit['dates'])}")
        print(f"Streak ending today: {streak} day(s)")


def main():
    habits = {}
    print("Habit Tracker - records stay in memory until you exit.")

    while True:
        print("\n1. Add habit\n2. Mark complete\n3. View habits\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_complete(habits)
        elif choice == "3":
            show_habits(habits)
        elif choice == "4":
            break
        else:
            print("Choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
