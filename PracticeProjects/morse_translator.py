# Translate letters and digits into Morse code and back.
# Practice: dictionary lookup, reverse mappings, splitting, and validation.


SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
CODES = (".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - "
         "..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.")
MORSE = dict(zip(SYMBOLS, CODES.split()))
LETTERS = {code: letter for letter, code in MORSE.items()}


def encode(text):
    words = []
    for word in text.upper().split():
        if any(character not in MORSE for character in word):
            raise ValueError("Only letters A-Z, digits, and whitespace are supported.")
        words.append(" ".join(MORSE[character] for character in word))
    return " / ".join(words)


def decode(text):
    if not text.strip():
        return ""
    words = []
    for word in text.split("/"):
        tokens = word.split()
        if not tokens or any(token not in LETTERS for token in tokens):
            raise ValueError("Use valid dot/dash codes, spaces between letters, and / between words.")
        words.append("".join(LETTERS[token] for token in tokens))
    return " ".join(words)


def main():
    print("Morse Translator - word separators are written as /.")
    while True:
        print("\n1. Encode text\n2. Decode Morse\n3. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print(f"Morse: {encode(input('Text: '))}")
            elif choice == "2":
                print(f"Text: {decode(input('Morse: '))}")
            elif choice == "3":
                break
            else:
                print("Choose an option from 1 to 3.")
        except ValueError as error:
            print(f"Invalid translation: {error}")


if __name__ == "__main__":
    main()
