
name = input('Enter your name:')
county = input('Enter your county:')
pet = input('What\'s your pet:')
language = input('Input your language:')

print(type(name))
print(type(county))
print(type(pet))
print(type(language))

if not isinstance(name, str) and not isinstance(county, str) and not isinstance(pet,str) and not isinstance(language, str):
    print('Should be a string')


details = f'my name is {name} and am from {county} my pet is {pet} and i speak {language}'