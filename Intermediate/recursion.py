#Recursion is a technique on which a function calls itself.
#Each calls works on smaller version of the original problem until it reaches a condition that stops the recusion.
#The stopping condition is called the base case.

def recursive_countdown(number):
    print(number)
recursive_countdown(10)

# Adding a Base Case

#You need to define the base case before making the function call. Without a reachable base case, the function will keep calling itself then python stops and raises RecursionError.

def recursive_countown(number):
    if number < 1:
        return
    print(number)
recursive_countown(5)

# Adding a Recursive Case

#Recursive case calls the function again with an argument that moves it toward the base case.

def recursive_countdon(number):
    if number < 1:
        return
    print(number)
    recursive_countdown(number - 1)
recursive_countdon(5)

#Changing the order of execution

#The positions of the recursive call changes when the numbers are printed.
#If the print() call comes after the recursive call the function prints the numbers in ascending order.

def recursive_countdwn(number):
    if number < 1:
        return
    recursive_countdown(number -1)
    print(number)
    recursive_countdwn(5)

# CallStack

#Is a last-in, First out(LIFO) data structure that python uses to keep track of active function calls.
#Python adds a frame for that call to the top of the stack.
#The frame contains information  such as the functions arguments and local variables.

# Tracing the CallStack

def recursive_countdow(number):
    print(f"Function call started for number: {number}")
    if number < 1:
        print("Base Reached")
        return
    print(f"Calling recursive countdown with number: {number - 1}")
    recursive_countdow(number - 1)
    print(f"Function calls completed for number: {number}")
recursive_countdow(3)