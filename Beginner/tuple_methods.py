
# 1. count() - determines how many times an item appears in a Tuple.

languages = ('python', 'java', 'c', 'rust', 'python')
print(languages.count('python')) # 2
print(languages.count('javascript')) # 0
#print(languages.count()) # TypeError: tuple.count() takes exactly one argument (0 given)
# if no argument passed in count() it will return TypeError
# if the value is not present in the Tuple count() will return 0

# 2. index() - used to find the index where a particular item is present in a Tuple.
languages = ('java', 'python', 'java', 'python', 'rust')
print(languages.index('python'))
#print(languages.index('Go')) # ValueError: tuple.index(x): x not in tuple
# if the specified item cannot be found it raises a ValueError

# you can also use index() method to pass in optional start and stop index arguments.
language = ('rust', 'java', 'python', 'c', 'rust', 'python')
print(languages.index('python', 3))

# 3. sorted() - creates a list of sorted values.
numbers = (64,96,3,89,22,90,3,0,3,6,1,)
print(sorted(numbers)) # [0, 1, 3, 3, 3, 6, 22, 64, 89, 90, 96]

# 4. reverse() - reverses the order of a tuple
reversed = ('python', 'java', 'javascript', 'rust', 'c')
print(sorted(reversed, reverse = True)) # ['rust', 'python', 'javascript', 'java', 'c']