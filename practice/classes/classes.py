class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.times_feed = 0

    def bark(self):
        return f'{self.name} says woof woof'

    def feed(self):
        self.times_feed += 1
        return f'{self.name} has been feed {self.times_feed} times'

    def __str__(self) -> str:
        return f'{self.name} is in {self.color} and eats {self.times_feed}'

my_dog = Dog('antony','black')
her_dog = Dog('joshua','blue')

print(f"My Dog is called {my_dog.name}")
print(f"\nMy Dog({my_dog.name}) is {my_dog.color} in color")

print(f"\nMy Dog is called {her_dog.name}")
print(f"\nMy Dog({her_dog.name}) is {her_dog.color} in color")

print(my_dog.bark())
print(her_dog.bark())

print(my_dog.feed())
print(her_dog.feed())
print(my_dog.feed())

print(getattr(my_dog,'name'))
print(getattr(her_dog,'color'))
print(hasattr(her_dog,'flue'))
print(hasattr(my_dog,'name'))

setattr(my_dog,'age',300)
setattr(her_dog,'age',100)
print(her_dog)
print(my_dog.age)
print(her_dog.age)