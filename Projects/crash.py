import os

question = input('Do You Love Me?(yes or no):')
answer = question.lower()
try:
    if answer != 'yes':
        os.remove("data.txt")
except PermissionError:
    print('Permission Denied')
else:
    print('Me Too')