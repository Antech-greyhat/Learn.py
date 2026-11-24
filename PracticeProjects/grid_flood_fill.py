# Replace a connected region of matching characters in a small grid.
# Practice: nested lists, stacks, bounds checks, and depth-first traversal.
import json


def flood_fill(grid, row, column, replacement):
    if not isinstance(grid, list) or not 1 <= len(grid) <= 30:
        raise ValueError("Grid must contain from 1 to 30 text rows.")
    if any(not isinstance(line, str) or not 1 <= len(line) <= 30 for line in grid):
        raise ValueError("Each row must have from 1 to 30 characters.")
    width = len(grid[0])
    if any(len(line) != width for line in grid):
        raise ValueError("Grid rows must have equal lengths.")
    if type(row) is not int or type(column) is not int or not (0 <= row < len(grid) and 0 <= column < width):
        raise ValueError("Starting row or column is outside the grid.")
    if not isinstance(replacement, str) or len(replacement) != 1:
        raise ValueError("Replacement must be one character.")
    result = [list(line) for line in grid]
    original = result[row][column]
    if original == replacement:
        return list(grid)
    stack = [(row, column)]
    result[row][column] = replacement
    while stack:
        current_row, current_column = stack.pop()
        for next_row, next_column in ((current_row - 1, current_column), (current_row + 1, current_column),
                                      (current_row, current_column - 1), (current_row, current_column + 1)):
            if 0 <= next_row < len(grid) and 0 <= next_column < width:
                if result[next_row][next_column] == original:
                    # Mark when pushing so no cell enters the stack twice.
                    result[next_row][next_column] = replacement
                    stack.append((next_row, next_column))
    return ["".join(line) for line in result]


def main():
    print('Grid Flood Fill - JSON example: ["aa#", "a##", "#aa"].')
    while True:
        text = input("Grid JSON (q to quit): ").strip()
        if text.lower() == "q":
            break
        try:
            grid = json.loads(text)
            row = int(input("Starting row (0-based): "))
            column = int(input("Starting column (0-based): "))
            replacement = input("Replacement character: ")
            for line in flood_fill(grid, row, column, replacement):
                print(line)
        except (ValueError, RecursionError) as error:
            print(f"Invalid fill: {error}")


if __name__ == "__main__":
    main()
