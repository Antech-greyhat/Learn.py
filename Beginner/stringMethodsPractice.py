# practice in string methods.
# .upper(): returns all strings in capital/ uppercase.
my_str = "I love python"
uppercase_str = my_str.upper()
print(uppercase_str) # output : I LOVE PYTHON

# .lower(): returns all strings in lowercase.

my_str = 'Am Learning python and i love it'
lowercase_str = my_str.lower()
print(lowercase_str) # output: am learning python and i love it

# .strip() : Returns a new string with the specified leading and trailing characters removed.
# If no argument is passed it removes leading and trailing whitespace.
my_str = ' i love eating '
strip_str = my_str.strip()
print(strip_str) # output: i love eating

# .replace(old, new):  Returns a new string with all occurrences of old replaced by new.
my_str = "hello world"
replaced_str = my_str.replace("hello", "hi")
print(replaced_str) # hi world

#.split(separator): Splits a string on a specified separator into a list of strings.
# A list groups values between square brackets. If no separator is specified, split() splits on whitespace.

my_str = "hello world"
split_str = my_str.split()
print(split_str) # output: ['hello', 'world']

# .join(): Joins the strings in a collection into a single string with a separator.
my_list = ["am", 'antony']
joined_list = ' '.join(my_list)
print(joined_list) # output: am antony

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

my_str = 'hello world'
starts_with_str = my_str.startswith("hello")
print(starts_with_str) # output: True

my_str = 'love python'
start_str = my_str.startswith("python")
print(start_str) # output: False

# .endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
my_str = "mangoes apples"
endswith_str = my_str.endswith('apples')
print(endswith_str) # output: True

my_str = 'python javascript'
end_str = my_str.endswith("python")
print(end_str) # output: False

# .find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
my_str = " i love python lol"
find_str1 = my_str.find("love")
find_str2 = my_str.find("python")
find_str3 = my_str.find("i")
find_str4 = my_str.find("javascript")
print(find_str1) # output: 3
print(find_str2) # output: 8
print(find_str3) # output: 1
print(find_str4) # output: -1

# .count(substring): Returns the number of times a substring appears in a string.
my_str = 'python'
count_str = my_str.count("n")
count_str2 = my_str.count('a')
print(count_str) # output: 1
print(count_str2) # output: 0

# .capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
my_str = "programming"
capitalize_str = my_str.capitalize()
my_str1 = "PYTHON"
capitalized_str1 = my_str1.capitalize()
print(capitalized_str1) #output: Python
print(capitalize_str)  #output: Programming

# .isupper(): Returns True if all letters in the string are uppercase and False if not.
my_str = "python"
my_str1 = "PYTHON"
upper_str = my_str.isupper()
upper_str1 = my_str1.isupper()
print(upper_str) # output: False
print(upper_str1) # output: True

# .islower(): Returns True if all letters in the string are lowercase and False if not.
my_str = "code"
my_str1 = "CODE"
lower_str = my_str.islower()
lower_str1 = my_str1.islower()
print(lower_str) # output: True
print(lower_str1) #output: False

# .title() : returns a new string with the first letter of each word  capitalized.

my_str = "python programming"
title_str = my_str.title()
print(title_str) # output: Python Programming