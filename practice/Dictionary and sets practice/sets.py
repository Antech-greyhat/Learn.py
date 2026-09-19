
numbers = {1,2,2,3,4,4,4,5}

unique_numbers = set(numbers)
print(unique_numbers) # {1, 2, 3, 4, 5}
unique_numbers.add(10)
print(unique_numbers)
unique_numbers.add(10)
print(unique_numbers)

set_a = {1,2,3,4}
set_b = {3,4,5,6}
intersection = set_a & set_b
print(intersection) #{3, 4}

union = set_a | set_b
print(union) # {1, 2, 3, 4, 5, 6}