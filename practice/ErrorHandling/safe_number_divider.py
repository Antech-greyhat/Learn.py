# Error Handling:

try:
    number1 = int(input('Enter 1st Number:'))
    number2 = int(input('Enter the 2nd Number:'))
    result = number1/number2
    
except ValueError:
    print('Please Enter a valid number.')
except ZeroDivisionError:
    print('Cannot Divide By Zero.')
else:
    print(f'Division Successful: {result:.1f}')