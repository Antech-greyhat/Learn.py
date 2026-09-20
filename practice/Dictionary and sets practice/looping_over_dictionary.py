
contact = {
    'name': 'antony',
    'number': '9090',
    'age': 20
}

# looping over keys:
for key in contact:
    print(key)

# or use .keys() :
print(contact.values())

# looping over values

for value in contact.values():
    print(value)
# or use .value():
print(contact.values())

# looping both values and keys:
for key,value in contact.items():
    print(f'{key}: {value}')

# or using this:
print(contact.items())