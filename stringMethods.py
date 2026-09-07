# A method is a function that you call on a value.
# To call a string method, write the string or its variable name followed by a dot and the method call.
# Here are some common string methods:
# >> upper(): Returns a new string with all characters converted to uppercase.
# Example Code

my_str = 'hello world'
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

# >> lower(): Returns a new string with all characters converted to lowercase.
# Example Code

my_str = 'Hello World'
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

# >> strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
# Example Code

my_str = '  hello world  '
trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

# >> replace(old, new): Returns a new string with all occurrences of old replaced by new.
# Example Code

my_str = 'hello world'
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

# >> split(separator): Splits a string on a specified separator into a list of strings. A list groups values between square brackets. If no separator is specified, split() splits on whitespace.
# Example Code:

my_str = 'hello world'
split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# >> join(): Joins the strings in a collection into a single string with a separator.
# Example Code:

my_list = ['hello', 'world']
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

# >> startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.
# Example Code

my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

# >> endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
# Example Code

my_str = 'hello world'
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

# >> find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
# Example Code

my_str = 'hello world'
world_index = my_str.find('world')
print(world_index)  # 6

# >> count(substring): Returns the number of times a substring appears in a string.
# Example Code

my_str = 'hello world'
o_count = my_str.count('o')
print(o_count)  # 2

# >> capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
# Example Code

my_str = 'hello world'
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
# >> isupper(): Returns True if all letters in the string are uppercase and False if not.
# Example Code

my_str = 'hello world'
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# >> islower(): Returns True if all letters in the string are lowercase and False if not.
# Example Code

my_str = 'hello world'
is_all_lower = my_str.islower()
print(is_all_lower)  # True

# >> title(): Returns a new string with the first letter of each word capitalized.
# Example Code

my_str = 'hello world'
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World