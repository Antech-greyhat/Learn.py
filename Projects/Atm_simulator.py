def withdraw(balance, amount):
    if amount < 0:
        raise ValueError('Amount Cannot be Negative')
    if amount > balance:
        raise ValueError('Insufficient Funds')
    return balance - amount


starting_balance = 1000

try:
    while True:
        user_amount = input('Enter Amount:')
        try:
            user_float = float(user_amount)
            balance = withdraw(starting_balance, user_float)
            print(f"Balance is: {balance}")
            break
        except ValueError as e:
            print(e)
finally:
    print('Transaction Attempt Completed.')