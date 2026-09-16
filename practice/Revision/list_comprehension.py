# list comprehensions - a shortcut for writing list.

squares_loop = []

for num in range(1, 11):
    squares_loop.append(num ** 2)

print(squares_loop)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares_comprehension = [num ** 2 for num in range(1, 11)]
print(squares_comprehension)