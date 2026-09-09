# using type() to check whether integer and whether float
# for integers
my_int_1 = 57
my_int_2 = -175
print(type(my_int_1)) # output: integer
print(type(my_int_2)) # output: integer

# for floats
my_float_1 = 15.976
my_float_2 = 100.78
print(type(my_float_1)) #output : float
print(type(my_float_2)) #output : float

# here is how to perform addition on integers
my_int_1 = 50
my_int_2 = 57
total_int = my_int_1 + my_int_2
print("Integer Addition is:", total_int) # output: Integer Addition is: 107

# performing subtraction in integers
my_int_1 = 100
my_int_2 = 99
subtraction_int = my_int_1 - my_int_2
print("Integer Subtraction is:", subtraction_int) # output: Integer Subtraction is: 1

# addition of Floats
float_1 = 10.11
float_2 = 20.99
sum_float = float_1 + float_2
print('Sum of Floats is:', sum_float) # output: Sum of Floats is: 31.099999999999998

# substraction of floats
float_1 = 100.22
float_2 = 25.77
sub_float = float_1 - float_2
print('Subtraction of Floats is:', sub_float) # output: ubtraction of Floats is: 74.45

# Division on floats
float_1 = 100
float_2 = 20
div_float = float_1 / float_2
print("Division of Float is:", div_float) # output: Division of Float is: 5.0

# Multiplication of floats
float_1 = 10
float_2 = 19
mult_float = float_1 * float_2
print("Multiplication of Floats is:", mult_float) #output: Multiplication of Floats is: 190

# NOTE: If you add an Integer and a Float the result is automatically converted to a Float
my_init = 60
my_float = 70.11
sum_int_and_float = my_init + my_float
print(sum_int_and_float) # output: 130.11
print(type(sum_int_and_float)) # output: <class 'float'>
# Also for all other Arithmetics: subtraction , multiplication and Division.