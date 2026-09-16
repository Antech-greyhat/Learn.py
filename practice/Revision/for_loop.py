# revision for loops - repeats code for each item in a collection.

foods = ['Rice', 'Meat', 'Ugali', 'Eggs', 'Githeri']
for food in foods:
    print(f'I enjoy eating {food}')

foods = ['Rice', 'Meat', 'Ugali', 'Eggs', 'Githeri']
drinks = ['soda', 'water', 'wine', 'tea', 'changaa']
# nesting for loop
for food in foods:
    for drink in drinks:
        print(f'When you eat {food}, take {drink} as your drink')