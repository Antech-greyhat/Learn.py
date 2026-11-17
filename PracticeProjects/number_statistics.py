# Summarize whole numbers and search the sorted list.
# Practice: lists, sets, sorting, functions, and binary search.


def parse_numbers(text):
    if not text.strip():
        raise ValueError("Enter at least one number.")
    return [int(value.strip()) for value in text.split(",")]


def get_statistics(numbers):
    if not numbers:
        raise ValueError("The number list cannot be empty.")

    ordered = sorted(numbers)
    count = len(ordered)
    middle = count // 2
    if count % 2:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2

    return {
        "count": count,
        "unique": len(set(numbers)),
        "total": sum(numbers),
        "minimum": ordered[0],
        "maximum": ordered[-1],
        "mean": sum(numbers) / count,
        "median": median,
    }


def binary_search(numbers, target):
    # Binary search requires an ascending list.
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def main():
    print("Number Statistics")
    while True:
        try:
            numbers = parse_numbers(input("Enter whole numbers separated by commas: "))
            break
        except ValueError:
            print("Enter one or more whole numbers, such as 4, -2, 7.")

    ordered = sorted(numbers)
    print(f"Sorted numbers: {ordered}")
    for name, value in get_statistics(numbers).items():
        print(f"{name.title()}: {value:g}")

    while True:
        text = input("Search for a whole number (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            target = int(text)
        except ValueError:
            print("Enter a whole number.")
            continue

        index = binary_search(ordered, target)
        if index == -1:
            print("Number not found.")
        else:
            print(f"Found at sorted index: {index}")


if __name__ == "__main__":
    main()
