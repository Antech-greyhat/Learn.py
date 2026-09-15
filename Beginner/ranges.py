# range() function is used to generate a sequence of integers. it is immutable.
# syntax:
# range(start,stop,step)

# the required stop argument is an integer that represents the endpoint for the sequence of numbers being generated.
# the stop argument is always non-inclusive.

for num in range(3):
     print(num) # this generates a sequence of numbers between 0 and 2.

# if the start argument is not specified then the default is 0 otherwise you can use start optinally.

for num in range(1,5):
    print(num) # generates sequence of integers between 1 and 4

# by default sequence of integer increment by 1 but you can change with using the stop argument.

for num in range(2,11,2):
    print(num) # generates sequence of even integers between 2 and 10.

# if no argument passed on range() it returns TypeError and only accepts integer as arguments.

# example of sequence of integers in decrementing order
for num in range(40,0,-10):
    print(num)

# to generate a list of integers pass a range to the list() constructor:

numbers = list(range(2,11,2))
print(numbers) # [2, 4, 6, 8, 10]