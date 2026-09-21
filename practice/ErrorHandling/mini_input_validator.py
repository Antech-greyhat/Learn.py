
def get_positive_number(number):
    while True:
        user_input = int(input('Input A positive Number: '))
        try:
            number = float(user_input)
            if number > 0:
                return number
            else:
                print('Error: The number must be Greater than 0. Try again!')
        except ValueError:
            print(f"Error: {user_input} is not a valid number. Try again!")

result = get_positive_number(5)
print(f"\nsuccess! you entered: {result}")