# Guess a hidden word before making six wrong guesses.
# Practice: strings, sets, loops, functions, and random.
import random


WORDS = ("python", "variable", "function", "dictionary", "inheritance", "recursion")


def play_round(word):
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < 6:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\nWord: {display}")
        print(f"Wrong guesses left: {6 - wrong_guesses}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters)) or 'none'}")

        guess = input("Guess one letter (quit to end the round): ").strip().lower()
        if guess == "quit":
            print(f"Round ended. The word was {word}.")
            return
        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Enter one letter from a to z.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess not in word:
            wrong_guesses += 1
            print("That letter is not in the word.")

        # A set removes repeated letters from the word.
        if set(word).issubset(guessed_letters):
            print(f"You won! The word was {word}.")
            return

    print(f"You lost. The word was {word}.")


def main():
    print("Hangman")
    while True:
        play_round(random.choice(WORDS))
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
