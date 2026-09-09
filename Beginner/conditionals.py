# How Do Conditional Statements and Logical Operators Work?
# Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.
# Comparison operators are operators that let you compare two or more values, and return a boolean value.
# Here's a table with the comparison operators in Python:

# ==	Equal	Checks if two values are equal
# !=	Not equal	Checks if two values are not equal
# >	Greater than	Checks if the value on the left is greater than the value on the right
# <	Less than	Checks if the value on the left is less than the value on the right
# >=	Greater than or equal	Checks if the value on the left is greater than or equal to the value on the right
# <=	Less than or equal	Checks if the value on the left is less than or equal to the value on the right

# Example Code

print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True

# In Python, the most basic conditional is the if statement. Here's the basic syntax:
# if condition:
#     pass # Code to execute if condition is True
# if statements start with the if keyword.
#
# condition is an expression that evaluates to True or False, followed by a colon (:).
#
# The body of the if statement constitutes a code block, which is a group of statements that belong together. Spaces at the beginning of a line are called indentation. In Python, indentation determines which statements belong to a code block.

age = 18
if age >= 18:
    print('You are an adult') # You are an adult
# The four spaces before print('You are an adult') indent that line and place it inside the if block.
# The following code would raise an IndentationError, which is Python's way to signal that indentation is required at a certain point of the code:

age = 18
if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3

# Blocks are also found in loops and functions, which you'll learn about in future lessons.
# Going back to our example, if age is anything less than 18, nothing is printed in the terminal:

age = 12
if age >= 18:
  print('You are an adult') # Nothing shows up in the terminal
# But what if you also want to print something if age is less than 18? That's where the else clause comes in. The else clause runs when the if condition is false. Here's the syntax for an if…else statement:

if condition:
#    pass # Code to execute if condition is True
else:
#    pass # Code to execute if condition is False

age = 12
if age >= 18:
    print('You are an adult')
else:
#     print('You are not an adult yet') # You are not an adult yet
# Note that you cannot place any statements between the if block and the else clause. The following code would raise a SyntaxError:

age = 12
if age >= 18:
     print('You are an adult')
print('Almost there!')
else: # SyntaxError: invalid syntax
     print('You are not an adult yet')
# There might be situations in which you want to account for multiple conditions. To do that, Python lets you extend your if statement with the elif (else if) keyword.

# Here's the syntax:

 #if condition1:
#    pass # Code to execute if condition1 is True
# elif condition2:
#    pass # Code to execute if condition1 is False and condition2 is True
# else:
#    pass # Code to execute if all conditions are False

age = 12
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child

age = 2
if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
#     print('You are a toddler or an infant') # You are a toddler or an infant