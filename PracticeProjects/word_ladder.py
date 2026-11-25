# Find the shortest chain of words that changes one letter at each step.
# Practice: sets, breadth-first search, queues, and parent reconstruction.
from collections import deque


WORDS = {"cold", "cord", "card", "ward", "warm", "word", "worm",
         "wood", "good", "gold", "bold", "bald"}


def find_ladder(start, goal, words):
    start, goal = start.strip().lower(), goal.strip().lower()
    if start not in words or goal not in words or len(start) != len(goal):
        raise ValueError("Both endpoints must be dictionary words of the same length.")
    queue = deque([start])
    parents = {start: None}
    candidates = sorted(word for word in words if len(word) == len(start))
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return list(reversed(path))
        for word in candidates:
            if word not in parents and sum(a != b for a, b in zip(current, word)) == 1:
                parents[word] = current
                queue.append(word)
    return []


def main():
    print("Word Ladder - only words in the small built-in dictionary are used.")
    print(f"Words: {', '.join(sorted(WORDS))}")
    while True:
        start = input("Start word (q to quit): ").strip()
        if start.lower() == "q":
            break
        goal = input("Goal word: ")
        try:
            path = find_ladder(start, goal, WORDS)
            if path:
                print(f"Ladder: {' -> '.join(path)} | Changes: {len(path) - 1}")
            else:
                print("No ladder connects these words.")
        except ValueError as error:
            print(f"Invalid ladder: {error}")


if __name__ == "__main__":
    main()
