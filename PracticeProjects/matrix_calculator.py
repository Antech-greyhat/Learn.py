# Transpose, add, and multiply small rectangular matrices without NumPy.
# Practice: nested lists, dimensions, comprehensions, JSON, and dot products.
import json
import math


def validate_matrix(matrix):
    if not isinstance(matrix, list) or not 1 <= len(matrix) <= 10:
        raise ValueError("A matrix must have from 1 to 10 rows.")
    if not isinstance(matrix[0], list) or not 1 <= len(matrix[0]) <= 10:
        raise ValueError("A matrix must have from 1 to 10 columns.")
    width = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != width:
            raise ValueError("All rows must have the same length.")
        for value in row:
            if type(value) not in (int, float) or not math.isfinite(value):
                raise ValueError("Matrix entries must be finite numbers.")
    return [[float(value) for value in row] for row in matrix]


def transpose(matrix):
    matrix = validate_matrix(matrix)
    return [list(column) for column in zip(*matrix)]


def add_matrices(left, right):
    left, right = validate_matrix(left), validate_matrix(right)
    if len(left) != len(right) or len(left[0]) != len(right[0]):
        raise ValueError("Addition requires equal dimensions.")
    result = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]
    return validate_matrix(result)


def multiply_matrices(left, right):
    left, right = validate_matrix(left), validate_matrix(right)
    if len(left[0]) != len(right):
        raise ValueError("Left columns must equal right rows for multiplication.")
    columns = list(zip(*right))
    result = [[math.fsum(a * b for a, b in zip(row, column)) for column in columns] for row in left]
    return validate_matrix(result)


def main():
    print("Matrix Calculator - JSON example: [[1, 2], [3, 4]].")
    while True:
        print("\n1. Transpose\n2. Add\n3. Multiply\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            break
        if choice not in ("1", "2", "3"):
            print("Choose an option from 1 to 4.")
            continue
        try:
            left = json.loads(input("First matrix: "))
            if choice == "1":
                result = transpose(left)
            else:
                right = json.loads(input("Second matrix: "))
                result = add_matrices(left, right) if choice == "2" else multiply_matrices(left, right)
            for row in result:
                print(" ".join(f"{value:g}" for value in row))
        except (ValueError, OverflowError, RecursionError) as error:
            print(f"Invalid matrix: {error}")


if __name__ == "__main__":
    main()
