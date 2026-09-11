
correct_username = 'admin'
correct_password = 'python123'

username = input('Enter your Username:')
password = input('Enter password:')

if username == correct_username and password == correct_password:
    print("Log in successful")
elif username != correct_username and password != correct_password:
    print('Invalid log in credentials')
elif username == correct_username or password != correct_password:
    print('Invalid log in credentials')
elif username != correct_username or password == correct_password:
    print('Invalid log in credentials')
else:
    print('Invalid details')

print(f'username entered is {username} and password entered is {password}')

