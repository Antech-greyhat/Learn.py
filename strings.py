# A string is a sequence of characters surrounded by either single or double quotation marks.
# Python treats both forms as strings, so you can use either one. Here are some examples:

my_str1_var = "name"
my_str2_var = 'name'

# If you need a multi-line string, you can use triple double quotes or single quotes:

my_str3_var = """ multiline
string
"""
my_str_6 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

#If your string contains either single or double quotation marks, then you have two options:

#Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

#Escape the single or double quotation mark in the string with a backslash (\).
# With this method, you can use either single or double quotation marks to wrap the string itself:

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

#using in operator: checks if a string contains one or more characters and returns a boolean that specifies whether the character or characters exist inthe string.

my_str = 'Hello, World'

#here is how to use the in operator:
print('Hello' in my_str)
print('Hey' in my_str)
print('hi' in my_str)
print('e' in my_str)
print('f' in my_str)
print('f' in my_str)
print('f' in my_str)

#using the len() operator : is used to get the length of a string. eg:

my_str10 = 'Hello World' #11

# indexing in strings. -- is getting the length of a string and working with individual characters. starts from 0. like in the my_str10 H is at index 0.
# here is how to use indexing and access individual characters.

my_str_index = "Hello World"
print(my_str_index[0]) # accesses index 0 which is H
print(my_str_index[1]) #e
print(my_str_index[2]) #l
print(my_str_index[7]) #o
# Also Negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on:
my_negative_str = 'Hello World'
print(my_negative_str[-1]) #d
print(my_negative_str[-2]) #l

#In Python, values can be mutable or immutable. A mutable value can be changed after it is created, while an immutable value cannot.

#You can point a variable at a new value, which is called reassignment, but you can't change an immutable value itself by adding, removing, or replacing any of its elements.

#Strings are immutable in Python. This means that you can reassign a different string to a variable:
greetings = 'hi'
greetings = 'hello'
print(greetings) #hello

# But direct modification of a string isn't allowed:
greetings = 'hi'
greetings[0] = 'H' #TypeError: 'str' object does not support item assignment