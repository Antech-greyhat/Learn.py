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
        return f"{self.name} is a {self.color} dog, fed {self.times_feed} everyday"

my_dog = Dog('antony','black')
her_dog = Dog('joshua','blue')

print(my_dog)
print(my_dog.bark())
print(her_dog)
print(her_dog.feed())
print(her_dog)
print(my_dog)
print(my_dog)
print(my_dog)
print(her_dog)