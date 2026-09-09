#isinstance() verifies that a particular variable is a specific type before performing operations on it.
# Example:

account_balance = "300"

isinstance(account_balance, int)  # will return False because it is a string.

#isinstance() takes a value and the type you want to check it against then it returns a boolean.
#here is the syntax: isinstance( the object/variable, the data type)

#isinstance() also allows to check for multiple types at once.

account_balance = 900
isinstance(account_balance, (int, float)) # it returns true since the data type is integer.

isinstance(account_balance, (str, float)) # returns false.