# Tuple are like list but they are locked you cannot change them once created making it good for data that should not be edited.

person = ('antony', 18, 'kenya')
print(person[0])
print(person[1])
print(person[2])

#person[1] = 20
#print(person[1]) #TypeError: 'tuple' object does not support item assignment

# you can also create a tuple using the tuple() method.

developer = 'antony'
print(tuple(developer)) # ('a', 'n', 't', 'o', 'n', 'y')