
fruits = ['apple','banana','cherry']

try:
    index_typed = int(input('Enter an Index Number:'))
    index = int(index_typed)
    print(f"The Fruit at {index} is {fruits[index]}")
except ValueError:
    print('Please Enter A Number!')
except IndexError:
    print(f'{index} is out of range.')