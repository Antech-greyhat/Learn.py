# Guess a number from 1 to 100 in seven attempts.
# Practice: input, loops, conditionals, functions, and exceptions.
import random


def play_round():
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 7:
        answer = input("Guess 1-100 (q to end this round): ").strip().lower()
        if answer == "q":
            print("Round ended.")
            return

        try:
            guess = int(answer)
        except ValueError:
            print("Enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number from 1 to 100.")
            continue

        # Only valid guesses use an attempt.
        attempts += 1
        if guess == secret_number:
            print(f"Correct! You used {attempts} attempt(s).")
            return

        hint = "Too low" if guess < secret_number else "Too high"
        print(f"{hint}. Attempts left: {7 - attempts}")

    print(f"No attempts left. The number was {secret_number}.")


def main():
    print("Number Guessing Game")
    while True:
        play_round()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
