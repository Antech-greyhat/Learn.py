# list comprehensuion allows you to create a new list in a single line by combining a loop and condition directly within square brackets.
from practice.discount_function import result

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers = [1,2,3,4,5]
result = [(num, 'even') if num % 2 == 0 else (num, 'old') for num in numbers]
print(result) # [(1, 'old'), (2, 'even'), (3, 'old'), (4, 'even'), (5, 'old')]

# 1. filter() function - another way to create a list starting from an existing iterable.

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
def is_long(word):
    return len(word)
long_word = list(filter(is_long()))
print(long_word)

# 2. map() function - takes an iterable and applies a function to each of its elements.

celsius = [0,10,20,30,40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32
fahrenheit = list(map(to_fahrenheit(celsius)))
print(fahrenheit)

# 3. map() function - is used to get the sum from an iterable like a list of tuple.
numbers = [5,10,15,20]
total = sum(numbers)
print(total)