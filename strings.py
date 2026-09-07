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