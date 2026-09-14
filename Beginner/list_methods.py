# 1. append() - used to add an item to the end of the list.

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

# we can also add a list to the end of another list using the append() method
number = [1,2,3,4,5]
even_numbers = [6,8,10]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, [6, 8, 10]]

# 2. extend() - similar to append but extend you can add multiple elements from one list to another.

numbers = [1,2,3,4,5]
even_numbers = [6,8,10,12]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10, 12]

# 3. insert() - inserts an element at a specific index in a list.
# insert method accepts 2 arguments the index where to insert and new item to insert.

numbers = [1,2,3,4,5]
numbers.insert(3,2.45)
print(numbers) #[1, 2, 3, 2.45, 4, 5]

# 4. remove() - removes an element from a list. it takes the value of the element to remove as an argument.
numbers = [10, 20, 30, 40, 50, 60, 60, 70]
numbers.remove(60)
numbers.remove(40)
print(numbers) # [10, 20, 30, 50, 60, 70]
# note that this method removes the first occurence of an item not all of them if they are duplicate.

# 5. pop() - removes an element at a specific index in the list.
# if you don't specify an element for pop method then the last element is removed.

numbers = [1,2,3,4,5]
numbers.pop(3)
print(number) # [1, 2, 3, 4, 5]

pop_number = [1,2,3,4]
pop_number.pop()
print(pop_number) # [1, 2, 3] - removes the last index

# 6. clear() - used to empty a list
clear_list = [1,2,3,4,5]
clear_list.clear()
print(clear_list) # []

# 7. sort() - used to sort elements in place.

numbers = [100, 20, 45, 19, 11, 32, 10]
numbers.sort()
print(numbers) # [10, 11, 19, 20, 32, 45, 100]

# 8. sorted() - works for any iterable and returns a new sorted list instead of modifying the original list.

random_numbers = [19, 34, 10, 4, 100]
sorted_numbers = sorted(random_numbers)
print(sorted_numbers) # [4, 10, 19, 34, 100]

# 9. reverse() - reverse a list
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_two = [10,9,8,7,6,5]
numbers.reverse()
numbers_two.reverse()
print(numbers) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(numbers_two) # [5, 6, 7, 8, 9, 10]

# 10. index() - used to find the first index where an element can be found in a list.
# if the element cannot be found the program throws ValueError.

programming_language = ['python', 'go', 'java', 'rust']

print(programming_language.index('python'))
print(programming_language.index('javascript')) # print(programming_language.index('javascript'))
#ValueError: list.index(x): x not in list

print(programming_language.index('Go')) # ValueError: list.index(x): x not in list - because is also case-sensitive