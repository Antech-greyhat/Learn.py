# for this task I will practice : String Methods, using Augmented operator, String slicing, conditionals and f string.
username = " AdminUser "
is_active = True
failed_attempts = 2
print(username)

stripped_username = username.strip() # using strip() string method to remove the spaces
print(stripped_username)

lowered_username = stripped_username.lower() # using lower() to convert the username to lowercase
print(lowered_username)

failed_attempts += 1 # if you change this augmented operator to -= the user will be an admin.
print(failed_attempts)

sliced_username = lowered_username[0:5]
print(sliced_username)

if failed_attempts >= 3 or is_active == False:
    print('Admin Access Denied')
elif username == sliced_username and failed_attempts == 0 or failed_attempts < 2 :
    print("Admin Access Granted")
else:
    print('You are a standard User')
print(f'Access Denied: for user {sliced_username} and many failed attempts to {failed_attempts}')

