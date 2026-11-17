# Count total words, unique words, and the five most common words.
# Practice: strings, list comprehensions, dictionaries, sets, and sorting.


def get_words(text):
    # Letters and digits form words; punctuation separates them.
    characters = [
        character.lower() if character.isalnum() else " "
        for character in text
    ]
    return "".join(characters).split()


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    text = input("Enter a line of text: ")
    words = get_words(text)
    if not words:
        print("No words found.")
        return

    counts = count_words(words)
    print(f"Characters including spaces: {len(text)}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(set(words))}")

    # Sort by count descending, then alphabetically for ties.
    common_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    print("Most common words:")
    for word, count in common_words[:5]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
