# Getters and Setters are methods that let you control how the attributes of a class are accessed and modified with getters.
# Getters you retrieve a value.
# Setters you set a value.
# Properties connect getters and setters and allow access to data. They act like attributes but behave like methods underhood.

# Main thing properties do is that they run extra logic behind the scenes when you get,set or delete values with them.
# Properties are preferred over method because mostly because of readability and convention making code cleaner and easier to read.
#You can also access properties simply using the dot notation.

#Decorator - is a function that modifies the functionalities of other functions or classes without changing their original code.
# We create a property using the ( @property)

class Circle:
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14 * (self.__radius **2)

my_circle = Circle(3)
print(my_circle.radius)
print(my_circle.area)

# <property_name>.setter => makes a setter.

class CircleOne:
    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self,value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self.__radius = value

my_circle_one = CircleOne(10)
print('Initial radius:',my_circle_one.radius)

my_circle_one.radius = 8
print('After modifying the radius:',my_circle_one.radius)

# Note: Inside the settler, you cannot use same name of the property when assigning a new value. This will lead to RecursionError.

# Deleter - enable you to control how you delete attribute.

class CircleTwo:
    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,value):
        if value <= 0:
            raise ValueError('Radius must be a positive number')
        self.__radius = value

    @radius.deleter
    def radius(self):
        print('Deleting Radius...')
        del self.__radius

my_circle_two = CircleTwo(33)
print('Initial Radius:',my_circle_two.radius)

del my_circle_two.radius
print('Radius Deleted!')
try:
    print(my_circle_two.radius)
except AttributeError as e:
    print("Error:",e)