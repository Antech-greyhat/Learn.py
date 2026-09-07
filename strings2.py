# String Concatenation and String interpolation

# Concatenating Strings
# In Python, you can combine multiple strings together with the plus (+) operator. This process is called string concatenation.
# Here's how to concatenate two strings with the plus operator:

my_str_1 = 'Hello'
my_str_2 = 'World'
str_plus_str = my_str_1 + ' ' + my_str_2  #the ' ' adds a space between hello and world upon concatenation.
print(str_plus_str)

# Repeating Strings
# You can also repeat a string by multiplying it with an integer using the * operator.
# The string is repeated the specified number of times:
sound = 'ha'
reapeted_sound = sound * 4
print(reapeted_sound) #hahahaha

# Concatenating Strings with Numbers
# Concatenation only works with strings. If you try to concatenate a string with a number, you'll get a TypeError:
# Example Code:
name = 'antony'
age = 99
name_and_age = name + age
print(name_and_age) #TypeError: can only concatenate str (not "int") to str

# the above code from line 22 to 25 prints an error so for you to run the whole code once you have to comment those lines or correct or remove them.

# using the str() functions to convert other data types to strings for string concatenation.
name = 'john'
age = 10
name_and_age = name + str(age) # converts the age from integer to a string.
print(name_and_age) #john10

# You can also use the augmented assignment operator for concatenation.
# This is represented by a plus and equals sign (+=), and performs both concatenation and assignment in one step.
# Here's it in action:
name = "john doe"
age = 100
name_and_age = name
name_and_age += str(age)
print(name_and_age) #john doe100