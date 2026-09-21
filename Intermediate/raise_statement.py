# Allows you to manually trigger exceptions in your code.
# Gives control when and how errors are generated, enabling you to create custom errors conditions and enforces specific program behaviours.
# At its most basic you can raise built-in exceptions or create custom error messages.

def check_age(age):
    if age < 0:
        raise ValueError('Age Cannot Be Negative')
    return age
try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# Raise can be used to re-raise the current exception, which is particularly useful in exception handling.
def process_data(data):
    try:
        result = int(data)
        return result*2
    except ValueError:
        print('Logging: Invalid data Received')
        raise
try:
    process_data('abc')
except ValueError:
    print('Handled at Higher Level')

# The keyword raise without arguments re-raises the current exception thats being handled. Allows you to log or perform cleanup while still propagating the error up the call stack.
# You can create and raise custom exceptions by defining your own exception classes:

class InsufficientFunds(Exception):
    def __init__(self,balance,amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'InsufficientFunds: ${balance} available, ${amount} requested')
def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientFunds(balance,amount)
    return balance - amount
try:
    new_balance = withdraw(100,150)
except InsufficientFunds as e:
   process_data(f'Transaction Failed: {e}')

# raise can also be used with the from keyword to chain exceptions.

def parse_config(filename):
    try:
        with open(filename,'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration File Is Missing') from None
    except ValueError as e:
        raise ValueError('Invalid Configuration format') from e
config = parse_config('config.txt')