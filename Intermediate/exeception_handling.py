# Exception handling is the process of catching and managing errors that occur during the execution of a program so code dont crash unexpectedly.
# Allows you to anticipate, catch and respond to errors in a structured way.
# common methods used: (try,except,else and finally)
# Using try and except:

try:
    x = 10 / 0
except ZeroDivisionError:
    print('You cant divide by Zero!')
# Try: anticipates that an error might occur.
# Except: runs if an error of the specified type is raised inside the try block.

# using else and finally:

try:
    x = 10/2
except ZeroDivisionError:
    print('You Cant Divide By Zero!')
else:
    print('Division Successful!')
finally:
    print('All is Done 🎉')

# Else: runs if no exception is raised in the try block.
# Finally: runs no matter what, whether an exception occurred.

# You can catch multiple exceptions with separate except blocks:
try:
    number = int('abc')
except ValueError:
    print('That was not a Valid Number!')
except ZeroDivisionError:
    print('Cant Divide by Zero!')

# The separate except makes your error responses more specific and useful.

# Using exception Object, which is aliased with another name with the as keyword, (e) as the alias for the error object.

try:
    x = 1/0
except ZeroDivisionError as e:
    print(f'Error Occurred: {e}') # Error Occurred: division by zero

# using the (e) let you access the actual error message or object for logging and debugging.

# you can also match multiple exceptions in a single except clause by specifying as a tuple:
try:
    number = int(input('Enter a number: '))
    result = 10 / number
except (ValueError,ZeroDivisionError) as e:
    print(f'Error Occurred: {e}')