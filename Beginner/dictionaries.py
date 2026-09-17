# Dictionary - are built in datastructures that store collection of key-value pairs. They work as real dictionary.
# in python you use a key to find it's corresponding value.
# syntax:
#dictionary = {
#    'key1' : 'value1'
#    'key2' : 'value2'
#    'Key3' : 'value3'
#}

# key must be unique in the dictionary and must be immutable data type.

pizza = {
    'name': 'margheritta pizza',
    'price': 8.9,
    'claories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
print(pizza) #{'name': 'margheritta pizza', 'price': 8.9, 'claories_per_slice': 250, 'toppings': ['mozzarella', 'basil']}
# dict() constructor - builds the dictionary from a sequence of key-value pairs.

pizza = dict([('name', 'margheritta'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
print(pizza) # {'name': 'margheritta', 'price': 8.9, 'calories_per_slice': 250, 'toppings': ['mozzarella', 'basil']}

# Accessing the value of a key-value pair we use the bracket notation - dictionary[key]
print(pizza['name']) #margheritta
print(pizza['toppings']) # ['mozzarella', 'basil']

# to update the value you just add the assignment operator followed by new value - dictionary[key] = 'value'
pizza['name'] = 'cookies'
pizza['calories_per_slice'] = 300
print(pizza) # {'name': 'cookies', 'price': 8.9, 'calories_per_slice': 300, 'toppings': ['mozzarella', 'basil']}