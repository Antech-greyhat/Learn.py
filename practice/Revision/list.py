# revision on list

foods = ['Rice', 'Meat', 'Ugali', 'Eggs', 'Githeri']

print(foods) # ['Rice', 'Meat', 'Ugali', 'Eggs', 'Githeri']

# printing the elements in the list using indexing
print(foods[-1]) #Githeri
print(foods[0]) #Rice
print(foods[3]) #Eggs
# print(foods[5]) #IndexError: list index out of range

# using append to add item in the list
foods.append('Tea') # remember that append takes exactly one argument
foods.append('Onion')
print(foods)

# we can add list to the end of another using append

numbers = [1,2,3,4,5]
even_numbers = [2,4,6,8]
numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [2, 4, 6, 8]]

# now we use the extend() method which works as append but you can add multiple elements in a list

drinks = ['soda', 'water', 'wine', 'tea']
sodas = ['fanta', 'coke', 'sprite', 'pepsi']

drinks.extend(sodas)
print(drinks) # ['soda', 'water', 'wine', 'tea', 'fanta', 'coke', 'sprite', 'pepsi']

numbers = [1,2,3,4,5]
even_numbers = [2,4,6,8]
numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 2, 4, 6, 8]