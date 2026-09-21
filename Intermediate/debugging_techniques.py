import pdb
# Debugging - is the process of identifying and resolving errors or bugs in your code.

# 1. using the print() function and f strings:
# it helps you understand the flow and state of variables.

def add(a,b):
    result = a+b
    print(f"Adding {a} and {b} gives {result}")
    return result
print(add(19,3))

# 2. using PDP module - is an interactive debugging were you have to import the module pdb as done in line 1:
def divide(a,b):
    pdb.set_trace() # this steps through the code inspect variables and understand the programs behavior.
    return a / b
print(divide(20,2))

# The pdb module gives an interactive prompt were when you use the help command you will see a list of commands.
# To continue the execution of the code use the Continue command or its aliases (cont/c)

# 3. IDE debugging - some IDES offer advanced debugging tools such as breakpoints, step execution and variable inspection.
