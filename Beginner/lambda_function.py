# lambda functions are anonymous functions. they are great when you need to use them in higher order function.

lambda num:num ** 2

numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
print(even_numbers) # [2, 4]