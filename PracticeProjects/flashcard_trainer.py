# Review Python terms in a shuffled flashcard deck.
# Practice: lists, dictionaries, strings, functions, and random.
import random


FLASHCARDS = [
    {"prompt": "Keyword used to define a function", "answer": "def"},
    {"prompt": "Collection that stores unique values", "answer": "set"},
    {"prompt": "Method used to add one item to a list", "answer": "append"},
    {"prompt": "Keyword used to handle an exception", "answer": "except"},
    {"prompt": "Function used to get the length of a collection", "answer": "len"},
    {"prompt": "Keyword used to create a class", "answer": "class"},
]


def study_cards(cards):
    score = 0
    missed_cards = []

    for number, card in enumerate(cards, start=1):
        print(f"\nCard {number}/{len(cards)}: {card['prompt']}")
        answer = input("Answer (blank to reveal): ").strip().lower()
        if answer == card["answer"].lower():
            score += 1
            print("Correct!")
        else:
            missed_cards.append(card)
            print(f"Answer: {card['answer']}")

    print(f"\nScore: {score}/{len(cards)}")
    if missed_cards:
        print("Review these terms:")
        for card in missed_cards:
            print(f"{card['prompt']}: {card['answer']}")


def main():
    # Shuffle a copy so the original deck keeps its order.
    cards = FLASHCARDS.copy()
    random.shuffle(cards)
    print("Python Flashcard Trainer")
    study_cards(cards)


if __name__ == "__main__":
    main()
