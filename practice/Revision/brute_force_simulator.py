target_password = 'antech2026'
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password: str = input('Enter password:')
    clean_password = password.strip().lower()
    if clean_password == " ":
        print('Error:password cannot be blank')
        continue
    if clean_password == target_password:
        print('Access granted! payload deployed.')
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f'Incorrect password! you have {remaining_attempts} attempts left')
    if attempts == max_attempts:
        print('Locked out of the session')