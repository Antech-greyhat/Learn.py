# list data type is an ordered sequence of elements that can be compromised of strings, numbers or even other lists.
# list are mutable and use zero-based indexing meaning that the first element of the list is at index zero.

cities = ['Nairobi', 'Mombasa', 'Machakos', 'Kisumu']
print(cities[2]) #Machakos

# to access elements starting from the end of the list instead of beggining at index 0 we use negative indexing.
programming_languages = ['python', 'java', 'javascript', 'rust']
print(programming_languages[-1]) #rust
print(programming_languages[-3]) #java

# using list() constructor - converts an iterable into a list.
developer = 'antony'
print(list(developer)) # ['a', 'n', 't', 'o', 'n', 'y']

# len() gets total length of elements in a list
developer = 'mwendwa'
print(len(developer)) # 7

# updating values in a list

programming_languages  = ['javascript', 'java', 'c', 'go']
programming_languages[0] = 'python'
print(programming_languages) # ['python', 'java', 'c', 'go']

#passing an index that is bound the program throws a NameError

programming_languages  = ['javascript', 'java', 'c', 'go']
#programming_languages[5] = 'python'
#print(programming_languages) #IndexError: list assignment index out of range

# removing elements from a list using del

developer = ['antony', 18, 'python developer']
del developer[1] # removes the element at index 1 which is the 18.
print(developer) # ['antony', 'python developer']

#using in to check if an element is inside a list and returns a boolean True or False

programming_languages = ['python', 'go', 'java', 'javascript']
print('rust' in programming_languages) #False
print('python' in programming_languages) # True

#nested lists

developer = ['antony', 25, ['python', 'rust', 'go']]
print(developer) # ['antony', 25, ['python', 'rust', 'go']]

# accessing the nested list you have to use index 2

developer = ['antony', 25, ['python', 'rust', 'go']]
print(developer[2]) # ['python', 'rust', 'go']

# accessing any element in the nested list you have first to enter the second list index then enter the elememt index.

developer = ['antony', 25, ['python', 'rust', 'go']]
print(developer[2][0]) # python
print(developer[2][1]) # rust
print(developer[2][2]) # go
#print(developer[2][3]) # IndexError: list index out of range

# unpacking values in a list - is used to assign values from a list to new variables.

developer = ['antony', 18, 'python developer']
name,age,role = developer
print(name) # antony
print(age) #18
print(role) # python developer

# using the asterisk(*) to collect any remaining elements from a list.
developer = ['antony', 18, ['python developer']]
# if number of variables on the left side of the assignment operator does not match the total numbers of items in the list then you will receive a ValueError

# slice(:) operator - access portions of a list by using the slice operator

deserts = ['cake', 'cookies', 'ice cream', 'pie', 'brownies']
print(deserts[1:4]) # ['cookies', 'ice cream', 'pie']

# can also use slice (:) operator to specify step interval which determines how much to increment between indices.

numbers = [1,2,3,4,5,6]
print(numbers[1::2]) # [2, 4, 6]
