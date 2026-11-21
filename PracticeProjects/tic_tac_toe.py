# Play tic tac toe with two players on the same terminal.
# Practice: nested lists, indexing, conditionals, functions, and loops.


def new_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def place_move(board, position, player):
    if player not in ("X", "O"):
        raise ValueError("Player must be X or O.")
    if type(position) is not int or not 1 <= position <= 9:
        raise ValueError("Choose a position from 1 to 9.")
    row, column = divmod(position - 1, 3)
    if board[row][column] != " ":
        raise ValueError("That position is already occupied.")
    board[row][column] = player


def get_winner(board):
    lines = list(board)
    lines.extend([[board[row][column] for row in range(3)] for column in range(3)])
    lines.append([board[index][index] for index in range(3)])
    lines.append([board[index][2 - index] for index in range(3)])
    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]
    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def show_board(board):
    for row_number, row in enumerate(board):
        labels = [cell if cell != " " else str(row_number * 3 + column + 1)
                  for column, cell in enumerate(row)]
        print(" | ".join(labels))
        if row_number < 2:
            print("--+---+--")


def main():
    print("Tic Tac Toe - two players; X starts. Enter q to quit.")
    while True:
        board = new_board()
        player = "X"
        while True:
            show_board(board)
            text = input(f"{player}, choose a position: ").strip().lower()
            if text == "q":
                return
            try:
                place_move(board, int(text), player)
            except ValueError as error:
                print(f"Invalid move: {error}")
                continue

            winner = get_winner(board)
            if winner or is_full(board):
                show_board(board)
                print(f"{winner} wins!" if winner else "It is a draw!")
                break
            # Only a successful move changes whose turn it is.
            player = "O" if player == "X" else "X"
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
