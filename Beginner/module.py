import math

# Library in python gives you written and re-usable code like functions, classes and data structures.

# 1. math - helpful function for performing more complex mathematical operations.
# 2. random - is helpful for generating numbers.
# 3. datetime - helpful for working with date and time.

# we use the import statement to import the libraries in our scripts.
# syntax : import module_name
#import math - should be at the top line of your program.

# syntax of calling a function from imported module :
# module_name.function_name()
print(math.sqrt(144))

# we can import module with different name (alias) we use as followed by the alias at the end.
# import math as m

# importing from different module you use from in the beginning.
# from math import radians,cos,sin
# from math import radians as rad, cos as c, sin as s

# you can use asterisk(*) if you want to import a module but you dont need to use the name of the module as a prefix.
#  from module_name import *
# from math import*