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