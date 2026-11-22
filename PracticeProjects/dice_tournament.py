# Simulate dice rolls and compare their observed frequencies.
# Practice: random.Random, Counter, loops, reproducibility, and statistics.
from collections import Counter
import random


def simulate_rolls(rolls, sides=6, seed=None):
    if type(rolls) is not int or not 1 <= rolls <= 100000:
        raise ValueError("Roll count must be from 1 to 100000.")
    if type(sides) is not int or not 2 <= sides <= 100:
        raise ValueError("Sides must be from 2 to 100.")
    generator = random.Random(seed)
    return Counter(generator.randint(1, sides) for _ in range(rolls))


def show_results(counts, sides):
    total = sum(counts.values())
    mean = sum(face * count for face, count in counts.items()) / total
    for face in range(1, sides + 1):
        count = counts[face]
        bar = "#" * round(count / total * 40)
        print(f"{face:>3}: {count:>6} | {count / total:6.2%} {bar}")
    print(f"Observed mean: {mean:.3f} | Theoretical mean: {(sides + 1) / 2:.3f}")


def main():
    print("Dice Tournament - simulated rolls, with an optional repeatable seed.")
    while True:
        text = input("Number of rolls (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            rolls = int(text)
            sides = int(input("Number of sides: "))
            seed_text = input("Whole-number seed (blank for random): ").strip()
            seed = int(seed_text) if seed_text else None
            show_results(simulate_rolls(rolls, sides, seed), sides)
        except ValueError as error:
            print(f"Invalid simulation: {error}")


if __name__ == "__main__":
    main()
