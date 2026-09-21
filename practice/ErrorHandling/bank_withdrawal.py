
def withdraw(balance,amount):
    if amount > balance:
        raise ValueError('Insufficient Funds!')
    return balance - amount
current_balance = 500
withdrawal_amount = 1000

try:
    new_balance = withdraw(current_balance,withdrawal_amount)
    print(f"Withdrawal successful: current balance is ${new_balance}")
except ValueError as e:
    shortfall = withdrawal_amount - current_balance
    print(f"Error: {e} needed ${shortfall} more for withdrawal to complete")
finally:
    print('Transaction Attempt Completed')