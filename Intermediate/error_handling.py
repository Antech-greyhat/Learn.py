# Recognizing common Python error messages helps you fix problems faster. Instead of guessing, read the error message carefully.
# It often tells you exactly what went wrong and where to look.
# you can comment in and out each line to get the Errors printed on terminal.

# Common error messages in python:
# 1. SyntaxError - a mistake of grammar rules in python:

#print('Hello world!'

# 2. NameError - mostly common on undefined variables:

#print(name)

# 3. TypeError - adding integer and string will result to name error:
sum = 5 + '5'
print(sum)

# 4. IndexError - trying to call an index out of range or printing:
my_list = [1,2,3]
print(my_list[5])

# 5. AttributeError - when you try to use a method on a variable type that does not pose it:
num = 42
num.append(5)
print(num)