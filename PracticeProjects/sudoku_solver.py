# Solve a 9x9 Sudoku using backtracking and the fewest-candidates heuristic.
# Practice: recursion, sets, nested lists, constraint checks, and copying.


def validate_grid(grid):
    if not isinstance(grid, list) or len(grid) != 9:
        raise ValueError("Sudoku must contain nine rows.")
    if any(not isinstance(row, list) or len(row) != 9 for row in grid):
        raise ValueError("Every Sudoku row must have nine cells.")
    if any(type(value) is not int or not 0 <= value <= 9 for row in grid for value in row):
        raise ValueError("Use whole numbers 0-9; zero means empty.")
    groups = list(grid) + [list(column) for column in zip(*grid)]
    for top in range(0, 9, 3):
        for left in range(0, 9, 3):
            groups.append([grid[row][column] for row in range(top, top + 3) for column in range(left, left + 3)])
    for group in groups:
        clues = [value for value in group if value]
        if len(clues) != len(set(clues)):
            raise ValueError("Starting clues conflict in a row, column, or 3x3 box.")


def solve_sudoku(grid):
    validate_grid(grid)
    board = [list(row) for row in grid]
    steps = 0

    def candidates(row, column):
        used = set(board[row]) | {board[index][column] for index in range(9)}
        top, left = row // 3 * 3, column // 3 * 3
        used.update(board[r][c] for r in range(top, top + 3) for c in range(left, left + 3))
        return sorted(set(range(1, 10)) - used)

    def search():
        nonlocal steps
        steps += 1
        if steps > 100000:
            raise ValueError("Search limit reached; try a puzzle with more clues.")
        best = None
        for row in range(9):
            for column in range(9):
                if board[row][column] == 0:
                    options = candidates(row, column)
                    if not options:
                        return False
                    if best is None or len(options) < len(best[2]):
                        best = row, column, options
        if best is None:
            return True
        row, column, options = best
        for value in options:
            board[row][column] = value
            if search():
                return True
        board[row][column] = 0
        return False

    return board if search() else None


def parse_grid(text):
    rows = [row.strip() for row in text.split(",")]
    if len(rows) != 9 or any(len(row) != 9 or any(char not in "0123456789" for char in row) for row in rows):
        raise ValueError("Enter nine comma-separated rows of nine digits each.")
    return [[int(char) for char in row] for row in rows]


def main():
    print("Sudoku Solver - zero marks an empty cell; returns one solution.")
    print("Example: 530070000,600195000,098000060,800060003,400803001,700020006,060000280,000419005,000080079")
    while True:
        text = input("Puzzle rows (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            solution = solve_sudoku(parse_grid(text))
            if solution is None:
                print("This puzzle has no solution.")
            else:
                print("Solution:")
                for row in solution:
                    print(" ".join(str(value) for value in row))
        except ValueError as error:
            print(f"Cannot solve puzzle: {error}")


if __name__ == "__main__":
    main()
