# Classes and Objects works together to organize and manage data.
# classes are templates used to create objects.
#syntax:
#class ClassName:
# you use the class keyword to create a class.
# Use PascalCase when naming classes.

class ClassName:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sample_method(self):
        print(self.name.upper())
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name.upper()} says woof woof!')

# syntax of creating objects from a class:

#object_1 = ClassName(attribute_1,attribute_2)
#object_2 = ClassName(attribute_1,attribute_2)

# you can also call any of the methods defined in the class from each object:

#object_1.method_name()
#object_2.method_name()

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name.upper()} says woof woof! I am {self.age} years old')
dog_1 = Dog('Jack',6)
dog_2 = Dog('Thatcher',10)

dog_1.bark()
dog_2.bark()

# Class is the template or the blueprint and an object is what is created using the template.
# Class defines what data and behavior the object should have and an object holds the actual data and uses the behaviour.
