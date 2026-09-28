# In opp is where developers treat everything in there code like a real world object.

# Principles of Object-Oriented Programming:
#  1. Encapsulation.
#  2. Inheritance.
#  3. Polymorphism.
#  4. Abstraction.

# 1. Encapsulation - is the bundling of the attributes and methods of an object into single unit, the class.
# With encapsulation, you can hide the internal state of the object behind a simple set of public methods and attributes that act like doors. Behind the doors there are private attributes and methods that control how data changes and who can see it.

# Here is an example of protecting Balance from direct Tempering:

class Wallet:
    def __init__(self,balance):
        self._balance = balance  # for internal use only.

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount # this adds to balance safely.

    def withdraw(self,amount):
        if 0 < amount <= self._balance:
            self._balance -= amount # Removes from balance safely.

# By Convection, Prefixing attribute and methods with a single underscore means they are meant for internal use.

# While a single underscore prefix is just a convection, prefixing attributes and methods with a double underscore effectively prevents that to be accessed from the outside of their class, making those attributes and methods private.

class AnotherWallet:
    def __init__(self,balance):
        self.__balance = balance # private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount # add to the balance safely.

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # remove from balance safely.

account = AnotherWallet(500)
#print(account.__balance) #AttributeError: 'AnotherWallet' object has no attribute '__balance'

# To get the current value of __balance you can define a get_balance method:

class ElseWallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


acct_one = ElseWallet(100)
acct_one.deposit(50)
print(acct_one.get_balance())  # 150

acct_two = ElseWallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance())  # 422

acct_two.deposit(150)
print(acct_two.get_balance())  # 572

# You can also define a private --validate method to check if every deposit or withdrawal amount is a positive number:

class ValidateWallet:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = ValidateWallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds