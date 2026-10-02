# With polymorphism, you have access to an interface where you can interact with many objects of the samekind.
# It allows metods in different classes to share the same name but perform different tasks.
# You call the same method name on different objects and each responds in its own way.

# syntax:

class A:
    def action(self):
        pass
class B:
    def action(self):
        pass
class C:
    def action(self):
        pass
#class().method

class Cat:
    def speak(self):
        return 'A cat meow'

class Bird:
    def speak(self):
        return "A bird tweet"

class Monkey:
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh'

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())

#Example 2:

class Twitter:
    def __init__(self,content):
        self.content = content
    def post(self):
        return f'Tweet: {self.content} (280 characters max)'

class Instagram:
    def __init__(self,content):
        self.content = content
    def post(self):
        return f"Instagram Post: '{self.content}' + Filters"

class Linkedin:
    def __init__(self,content):
        self.content = content
    def post(self):
        return f"LinkedIn Article: '{self.content}' (professional mode)"

def start(social_media):
    print(social_media.post())

#Instances.
tweet = Twitter('Just learned python polymorphism')
photo = Instagram('Hacking vibes')
article = Linkedin('Why OPP matters in 2026')

#polymorphic calls

start(tweet)
start(photo)
start(article)


# Inheritance based polymorphism - a parent class defines a method and multiple child classes override that child classes override that method in their own way.

class Animal:
    def speak(self):
        return 'Some generic sounds.'

class Cat:
    def speak(self):
        return 'A cat meow'

class Dog(Animal):
    def speak(self):
        return 'A dog barks woof woof'

class Monkey:
    def speak(self):
        return 'A monkey ooh aah'

# calling using a loop

animals = [Cat(), Dog(), Monkey()]
for animal in animals:
    print(animal.speak())