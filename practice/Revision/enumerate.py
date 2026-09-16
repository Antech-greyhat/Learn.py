# enumerate() - getting the index and the item together with its position number.

fruits = ['apple', 'mangoes', 'passion']

for index, fruit in enumerate(fruits, start=1):
    print(f'{index}:{fruit}')