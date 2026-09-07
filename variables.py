# variables are storage name locations. they help the programmer to store and re use information.
# below is a syntax of writting variables in python.

name = "antech" #these create a variable name with the value antech
age = 18  #these create a variable age with the value of 18 which is an interger.

# another thing to note is that a string is enclosed with either single quotes(') or double qoutes(").
#lets print the variables above

print(name)
print(age)

#using the keyword type while printing a variable tells us if is a string or an integer
print(type(name))  #string
print(type(age)) #integer

#finally there are rules of declaring variables:
# 1. can only start with a letter or an underscore(_) not a number.
# 2. can only contain alphanumeric characters and underscores.
# 3. they are case-sensitive eg: age, Age and AGE are very different.
# 4. cannot be on reserved python keywords eg: if, def, class.
# 5. they use Snake-case which means they should be in lowercase separated by underscores eg: my_variable_name.
# 6. note that breaking the variable rules when you run the script you will get a "syntax error".