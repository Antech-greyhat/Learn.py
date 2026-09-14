username = 'antech'
password = 1234

name = input('Enter name as username:')
clean_name = str(name)
print(clean_name)

passwd = input('enter password:')
passwd = int(passwd)

def check_login(entered_username, entered_password):

    if entered_username == username and entered_password == password:
        print('Log in Successful')
    else:
        print('Log in failed')

    return check_login
check_login(clean_name, passwd)