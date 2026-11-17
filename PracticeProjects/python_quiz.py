# Answer five questions and receive a percentage score.
# Practice: lists, dictionaries, tuples, enumerate, and functions.
QUESTIONS = [
    {
        "question": "Which type stores key-value pairs?",
        "options": ("list", "dict", "tuple"),
        "answer": 2,
    },
    {
        "question": "What is the result of 17 % 5?",
        "options": ("2", "3", "4"),
        "answer": 1,
    },
    {
        "question": "Which loop repeats while a condition is true?",
        "options": ("for", "while", "def"),
        "answer": 2,
    },
    {
        "question": "Which method adds one item to a list?",
        "options": ("append", "split", "get"),
        "answer": 1,
    },
    {
        "question": "Which collection stores unique values?",
        "options": ("tuple", "list", "set"),
        "answer": 3,
    },
]


def get_answer(options):
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            answer = int(input(f"Choose 1-{len(options)}: "))
        except ValueError:
            print("Enter a whole number.")
            continue

        if 1 <= answer <= len(options):
            return answer
        print("Choose one of the listed options.")


def main():
    score = 0
    print("Python Quiz")

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {number}: {question['question']}")
        answer = get_answer(question["options"])
        if answer == question["answer"]:
            score += 1
            print("Correct!")
        else:
            # Menu numbers start at 1; tuple indexes start at 0.
            correct_answer = question["options"][question["answer"] - 1]
            print(f"Incorrect. The answer is {correct_answer}.")

    percentage = score / len(QUESTIONS) * 100
    print(f"\nFinal score: {score}/{len(QUESTIONS)} ({percentage:.0f}%)")


if __name__ == "__main__":
    main()
