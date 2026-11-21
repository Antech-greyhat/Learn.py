# Keep events and show the time remaining or elapsed in UTC.
# Practice: timezone-aware dates, timedelta, dictionaries, and sorting.
from datetime import datetime, timezone


def parse_event_time(text):
    try:
        return datetime.strptime(text.strip(), "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    except ValueError as error:
        raise ValueError("Use a valid UTC date and time: YYYY-MM-DD HH:MM.") from error


def describe_countdown(event_time, now):
    if event_time.utcoffset() is None or now.utcoffset() is None:
        raise ValueError("Both times must include a timezone.")
    # Normalize to UTC before subtracting, including across daylight saving changes.
    delta = event_time.astimezone(timezone.utc) - now.astimezone(timezone.utc)
    seconds = int(abs(delta.total_seconds()))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    duration = f"{days}d {hours}h {minutes}m {seconds}s"
    if delta.total_seconds() > 0:
        return f"Starts in {duration}"
    if delta.total_seconds() < 0:
        return f"Started {duration} ago"
    return "Starts now"


def add_event(events, name, time_text):
    name = name.strip()
    key = name.lower()
    if not name:
        raise ValueError("Event name cannot be empty.")
    if key in events:
        raise ValueError("Event already exists.")
    events[key] = {"name": name, "time": parse_event_time(time_text)}


def show_events(events):
    if not events:
        print("No events yet.")
        return
    now = datetime.now(timezone.utc)
    for event in sorted(events.values(), key=lambda item: item["time"]):
        print(f"{event['name']} | {event['time']:%Y-%m-%d %H:%M} UTC")
        print(describe_countdown(event["time"], now))


def main():
    events = {}
    print("Event Countdown - all times are UTC; events last for this session.")
    while True:
        print("\n1. Add event\n2. View countdowns\n3. Remove event\n4. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Event name: ")
                time_text = input("UTC date and time (YYYY-MM-DD HH:MM): ")
                add_event(events, name, time_text)
                print("Event added.")
            elif choice == "2":
                show_events(events)
            elif choice == "3":
                key = input("Event name: ").strip().lower()
                if key not in events:
                    raise ValueError("Event not found.")
                print(f"Removed: {events.pop(key)['name']}")
            elif choice == "4":
                break
            else:
                print("Choose an option from 1 to 4.")
        except ValueError as error:
            print(f"Invalid event: {error}")


if __name__ == "__main__":
    main()
