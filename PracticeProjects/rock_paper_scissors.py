# Play against the computer and track wins, losses, and draws.
# Practice: dictionaries, conditionals, loops, functions, and random.
import random


BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def get_result(player, computer):
    if player == computer:
        return "draw"
    if BEATS[player] == computer:
        return "win"
    return "loss"


def main():
    scores = {"win": 0, "loss": 0, "draw": 0}
    print("Rock Paper Scissors")

    while True:
        player = input("Choose rock, paper, or scissors (q to quit): ").strip().lower()
        if player == "q":
            break
        if player not in BEATS:
            print("Choose rock, paper, or scissors.")
            continue

        computer = random.choice(tuple(BEATS))
        result = get_result(player, computer)
        scores[result] += 1
        print(f"Computer chose {computer}. Result: {result}.")
        print(f"Wins: {scores['win']} | Losses: {scores['loss']} | Draws: {scores['draw']}")

    print(f"Rounds played: {sum(scores.values())}")


if __name__ == "__main__":
    main()
