class BankAccount:
    def __init__(self,owner_name,starting_balance):
        self.owner_name = owner_name
        self.starting_balance = starting_balance
        self.transaction_count = 0

    def account_summary(self):
        return f'{self.owner_name} has a balance of Ksh:{self.starting_balance}'

    def deposit(self,amount):
        self.transaction_count += 1
        self.starting_balance += amount

    def __str__(self) -> str:
        return f"{self.owner_name}'s Account - Balance is Ksh:{self.starting_balance}, Transactions:{self.transaction_count}"



account_obj = BankAccount('antony',1000000)
account_obj1 = BankAccount('joshua',500000000)

account_obj.deposit(900)
account_obj1.deposit(1000)
account_obj1.deposit(100)

setattr(account_obj,'account_type','savings')
print(hasattr(account_obj1,'account_type'))
print(hasattr(account_obj,'name'))

print(account_obj1)
print(account_obj)