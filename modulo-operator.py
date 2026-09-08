# The Modulo Operator (%) returns the remainder when the value on the left is divided by the value on the right.

my_int_1 = 56
my_int_2 = 13
remainder_int = my_int_1 % my_int_2
print("The Remainder is:", remainder_int) # output: The Remainder is: 4

my_float_1 = 7.33
my_float_2 = 14.55
remainder_float = my_float_2 % my_float_1
print("Remainder is:", remainder_float) # output: Remainder is: 7.220000000000001

# Floor Division (//) divides two numbers and returns the greatest integer less than or equal to the result.
my_int_1 = 56
my_int_2 = 14
floor_int = my_int_1 // my_int_2
print(floor_int) #output: 4

my_float_1 = 5.63
my_float_2 = 4.2
floor_float = my_float_1 //my_float_2
print(floor_float) #output: 1.0

# Exponentiation (**) raises a number to the power of another.
my_int_1 = 60
my_int_2 = 7
exp_int = my_int_1 ** my_int_2
print(exp_int) # output: 2799360000000

my_float_1 = 45.236
my_float_2 = 5.8938
exp_float = my_float_1 ** my_float_2
print(exp_float) # output: 5716006985.03335

# Float() function returns a floatong point number constructed from the given number.
my_int = 79
my_float = float(my_int)
print(my_float) # output: 79.0
print(type(my_float)) # output: <class 'float'>

# Int() function returns an integer constructed from a given number.
my_float = 56.9047
my_int = int(my_float)
print(my_int) # output: 56
print(type(my_int)) #output: <class 'int'>

# Also, you can use the same built-in functions to convert a string into either a float or integer.
my_str = "67"
my_int = 77
int_str = int(my_str)
float_int = float(my_int)
print(int_str) # output: 67
print(float_int) # output: 77.0

# round() Rounds a number to the specified number of decimal places.
# By default this function rounds to the nearest integer, and returns a whole number with no decimal places.
my_int_1 = 4.8898
my_int_2 = 67.87
rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1) # rounds to one decimal place
print(rounded_int_1) #output: 5
print(rounded_int_2) #output: 67.9

# abs() returns the absolute value of a number.
num = -76
absolute_value = abs(num)
print(absolute_value) # output: 76

# pow() raises a number to the power of another or performs modular exponentiation.
result_1 = pow(2,3) # same as 2 **3
result_2 = pow(2,3,5) # same as (2 **3) %5
print(result_1) #output: 8
print(result_2) #output: 3