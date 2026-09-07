# string interpolation - is the process of inserting variables and expressions into a string.
# in python F-string (formatted string literals) allows you to handle interpolation with a compact and readable syntax.
# F-strings start with f (either lowercase or uppercase) before the quotes, and allow you to embed variables or expressions inside replacement fields indicated by curly braces ({}).
# Here's an example:

name = "john"
age = 30

name_and_age = f"My name is {name} and i am {age} years old"
print(name_and_age) #My name is john and i am 30 years old

num1 = 20
num2 = 99

print(f"The sum of {num1} and the sum of {num2} is {num1 + num2}") #The sum of 20 and the sum of 99 is 119

# Note how you don't need to convert non-string types with the str() function.
# In the example above, the value of the age, num1, and num2 variables is converted under the hood into a string during the interpolation process.