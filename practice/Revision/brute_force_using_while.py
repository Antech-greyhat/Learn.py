# revision on while loop.
target_password = "antech2026"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password: str = input('Enter Password:')
    clean_password = password.strip().lower()
    if clean_password == "":
        print('Error: Password cannot be blank')
        continue
    if clean_password == target_password:
        print('Access Granted! Payload deployed')
        break
    attempts += 1
    print(f'Wrong password remaining attempts: {max_attempts - attempts}')

if attempts == max_attempts:
    print('Intrusion Detected. System Locked.')