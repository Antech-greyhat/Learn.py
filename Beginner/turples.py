
# Tuple is a python data type used to create an ordered sequence of values. can also contain a mix of data types.

developer = ('antony', 18, 'python developer')

# Tuples are immutable meaning that the elements in a tuple cannot be changed once created. I f you try updating an item in tuple you will get a TypeError.

programming_languages = ('python', 'java', 'rust', 'go')
#programming_languages[0] = 'javascript'   # TypeError: 'tuple' object does not support item assignment

# to access element from a tuple you can use bracket notation and index number.
developer = ('antony', 'python developer', 20)
print(developer[1]) # python developer

# Remember to use a negative index to access an element from the end of a tuple:

food = ('rice', 'beans', 'meat', 'brownies')
print(food[-2]) # meat

# if you happen an to pass an index that exceeds or equals the length of the tuple you will get an IndexError:

drinks = ('soda', 'water', 'urine', 'spirit')
print(len(drinks)) # 4
#print(drinks[4]) # IndexError: tuple index out of range
#print(drinks[6]) # IndexError: tuple index out of range

# creating tuples by using the Tuple() contactor
developer = 'antony'
numbers = (1,2,3,4)
print(tuple(developer)) # ('a', 'n', 't', 'o', 'n', 'y')
print(tuple(numbers)) # (1, 2, 3, 4)

# for the tuple() constructor you can pass in different iterables like strings, lists and even other tuples.
# in Tuple we still use the in operator to check if an item is in the tuple

artist = ('wakadinali', 'jones', 'scar')
print('sewer' in artist) # False
print('jones' in artist) # True

# same as in list we can unpack items from a tuple

developer = ('antony', 18, 'python', 'linux')
#name,age = developer
#print(name)
#print(age)

# we can still use the asterisk(*) to collect remaining elements from tuple
# you can also use slice operator on tuple to extract a portion of it.
# removing item from a tuple is impossible and will throw a TypeError.

developer = ('antony', 20, 'python')
#del developer[1] # TypeError: 'tuple' object doesn't support item deletion

# use Tuple if you are working with a fixed and immutable collection of data.
# use list if you need a dynamic collection of elements where you can add, remove and update elements then you should use alist.

