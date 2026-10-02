# with inheritance a subclass(or child class) can use the attributes and methods of a base class(or parent class).
#This allows you to reuse the code, create clear class hierarchies, and customize behaviour without rewritting everything.
# Can customize by extending methods or overriding them in child class.
# Syntax:

class Parent:
#    #parent attributes and methods
class Child(Parent):
#    #child inherits, extends and overrides where necessary.

# For the child class to inherit from the parent class you have to pass the parent to the child pass.
#This is called single inheritance.

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

jack = Dog('jack')
print(jack.sound())
print(jack.bark)

# Here is overriding the sound() method from the parent animal.

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'
    def sound(self):
        return f"{self.name} barks {self.bark}"

joy = Dog('joy')
print(joy.sound())

# Multiple Inheritance - here a child class can inherit from more than one parent class.

# Syntax:

class Parent:
    #attributes and methods for parent.
class Child:
    #attributes and methods for child.
class GrandChild(Parent,Child):
    # grand child inherits from both parent and child.
    # grand child can combine or override behavior from each other.


class Walker:
    def walk(self):
        return 'I can walk on Land.'

class Swimmer:
    def swim(self):
        return 'I can swim in waters.'

class Amphibians:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        return f"I am {self.name} the Frog.{self.walk} and {self.swim}"

frog = Amphibians('joseph')
print(frog.introduce())