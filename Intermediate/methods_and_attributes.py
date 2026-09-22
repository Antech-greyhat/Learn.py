# 1. Attributes are variables that belong to an object, so they hold data:
# a. Instance attributes - are unique to each object created from a class and usually set them with the _init_ method.
# b. Class attributes - belong to the class itself and are shared by all instances of that class.
# use the dot notation to access the attributes.

class Dog:
    species = 'French Bulldog'    # class attribute
    def __init__(self,name):
        self.name = name   # instance attribute
print(Dog.species)
dog1 = Dog('Jack')
print(dog1.name)
print(dog1.species)

dog2 = Dog('Tom')
print(dog2.name)
print(dog2.species)

# NOTE: you can access class attributes from the class itself but you need to create an object and pass it data first before you can access instance attribute.

# 2. Methods - are functions defined inside a class with them any object from a class can perform actions that operate on or modify its own data.

class Dog:
    species = "French Bulldog"
    def __init__(self,name):
        self.name = name
        def bark(self):
            return f"{self.name} says woof woof!"
Jack = Dog('Jack')
Jill = Dog("Jill")