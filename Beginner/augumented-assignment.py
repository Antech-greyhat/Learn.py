# applies operation to a variable and stores the result back in the same variable all in one step.
# there are 2 syntax:
# 1. variable <operator> = value
# 2. variable = variable <operator> value

my_var = 5
my_var = my_var + 10
print(my_var) # output: 15

my_var = 5
my_var += 10
print(my_var) #15

#The subtraction assignment operator (-=) subtracts the right operand from the left variable and stores the difference in the left variable:
count = 14
count -= 3
print(count) # 11

#The multiplication assignment operator (*=) multiplies the left variable by the right operand and stores the product back in the left variable:
product = 65
product *= 7
print(product) # 455

#The division assignment operator (/=) divides the left variable by the right and stores the result back in the left variable:
price = 100
price /= 4
print(price) # 25.0

#The floor division operator (//=) floor‑divides the left variable by the right and stores the result back in the left variable:
total_pages = 23
total_pages //= 5
print(total_pages) # 4

#The modulo assignment operator (%=) computes the remainder of the left variable divided by the right and stores it back in the left variable:
bits = 35
bits %= 2
print(bits) # 1

#The exponentiation assignment operator (**=) raises the left variable to the power of the right and stores the result back in the left variable:
power = 2
power **= 3
print(power) # 8

#You can use some augmented assignment operators with strings, too. For example, the addition assignment operator makes it easy to concatenate strings:
greet = 'Hello'
greet += ' World'
print(greet) # Hello World

#And the multiplication assignment operator can be used to repeat a string:
greet = 'Hello'
greet *= 3
print(greet) # HelloHelloHello

#Other augmented assignments throw a TypeError when you use them with strings:

greet = 'Hello'
greet -= ' World'
print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str'