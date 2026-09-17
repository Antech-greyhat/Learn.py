pizza = {
    'name': 'pizza',
    'price': 8.9,
    'claories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
# 1. .get() - retrieves value associated with a key.
# syntax: dictionary.get(key,default) - the default value is set so you wont get an error if the key does not exist.

print(pizza.get('toppings', [])) #['mozzarella', 'basil']
# if the key does not exist it will return an empty list

print(pizza.get('spices', [])) # []

# 2. .key() - returns a view object with all keys in the dictionary respectively.
# syntax: dictionary.keys()

print(pizza.keys()) # dict_keys(['name', 'price', 'claories_per_slice', 'toppings'])

# 3. .values() - return a view object with all  values in the dictionary respectively.
# syntax: dictionaty.values()

print(pizza.values()) # dict_values(['pizza', 8.9, 250, ['mozzarella', 'basil']])

# 4. .items() - returns a view object with all the key-value pairs in the dictionary including both keys and values.
# syntax: dictionary.items

print(pizza.items()) # dict_items([('name', 'pizza'), ('price', 8.9), ('claories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

# 5. .clear() - removes all the key-value pairs from the dictionary.
# syntax: dictionary.clear()

pizza.clear()
print(pizza) # {}

# 6. .pop() - removes the key-value pair with the key that you specify as the first argument and returns its value.
# if the key does not exist it returns the default value that you specify as the argument.
# syntax: dictionary.pop()

print(pizza.pop('price' ,10)) # 10
#print(pizza.pop('total_price')) # KeyError: 'total_price'

# 7. .popitem() - removes the last inserted item.

# 8. .update() - updates the key values pairs with the key-value pairs of another dictionary.
pizza.update({'price': 150, 'total_price': 2000})
print(pizza) # {'price': 150, 'total_price': 2000}