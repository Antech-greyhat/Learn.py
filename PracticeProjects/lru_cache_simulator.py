# Simulate a cache that evicts the least recently used entry when full.
# Practice: OrderedDict, classes, ordering, and state changes.
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        if type(capacity) is not int or not 1 <= capacity <= 20:
            raise ValueError("Capacity must be a whole number from 1 to 20.")
        self.capacity = capacity
        self.entries = OrderedDict()

    def put(self, key, value):
        key = key.strip()
        if not key:
            raise ValueError("Key cannot be empty.")
        self.entries[key] = value
        self.entries.move_to_end(key)
        if len(self.entries) > self.capacity:
            return self.entries.popitem(last=False)
        return None

    def get(self, key):
        key = key.strip()
        if key not in self.entries:
            raise ValueError("Cache miss: key not found.")
        self.entries.move_to_end(key)
        return self.entries[key]

    def snapshot(self):
        return list(self.entries.items())


def main():
    print("LRU Cache Simulator - keys are case-sensitive; entries last for this session.")
    while True:
        text = input("Cache capacity (1-20, q to quit): ").strip()
        if text.lower() == "q":
            return
        try:
            cache = LRUCache(int(text))
            break
        except ValueError as error:
            print(f"Invalid capacity: {error}")
    while True:
        print("\n1. Put entry\n2. Get entry\n3. View oldest to newest\n4. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                key, value = input("Key: "), input("Value: ")
                evicted = cache.put(key, value)
                print(f"Evicted: {evicted[0]}" if evicted else "Entry stored.")
            elif choice == "2":
                print(f"Value: {cache.get(input('Key: '))}")
            elif choice == "3":
                if not cache.entries:
                    print("Cache is empty.")
                for key, value in cache.snapshot():
                    print(f"{key}: {value}")
            elif choice == "4":
                break
            else:
                print("Choose an option from 1 to 4.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
