# functions are reusable blocks of code that run when you call them.
# in python, we have some inbuilt function like: print(), int(), input().

# print:
print('Hello World')  #output: Hello world

#i int() this converts a number, boolean and numeric strings into an integer.
print(int(3.143))  #output: 3
print(int("20"))  #output: 20
print(int(True))  #output: 1

#input()  this lets the programmer  prompt the user for input
name = input('What is your name:')
print("Hello", name) #output: Hello plus the name entered.

# def >> allows you to write your own custom functions.
#syntax
#def name_of_the_function():
#code your function should execute
#example:

def greetings():
    print('Hello world') # this is the functions body

greetings() # this calls the function

def calcualte_sum(a,b): #this creates a function with parameters a and b.
    print(a + b)
calcualte_sum(3,5) #this calls the function and pass the arguments
#parameters are placeholder variables.
#Arguments are the value that you pass to a function when you call it.

# clear example without comments

def get_sum(x,y):
    print(x + y)
get_sum(10,35)

#note that calling a function without the correct number of arguments you will get a typeError

#get_sum(10)  #TypeError: get_sum() missing 1 required positional argument: 'y'

# functions also use a special return keyword to exit the function and return a value.
# python returns NONE by default if you dont use return.
# None is immutable and falsy which means it cannot be changed and evaluates to False in boolean context.

def add_sum(a,b):
    print(a + b)
my_sum = add_sum(10,55) #prints the output 65
print(my_sum) #None to fix this we have to use the return keyword.

def return_sum(m,n):
    return m + n
my_return_sum = return_sum(20,66)
print(my_return_sum) #output: 86

def return_sub(x,y):
    return x - y
my_sub= return_sub(30,19)
print(my_sub) #output: 21