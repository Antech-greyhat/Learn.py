

first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
clear_first_name = first_name.strip().lower()
clear_last_name = last_name.strip().lower()

print(clear_first_name)
print(clear_last_name)

length_first_name = len(clear_first_name)
print(length_first_name)
length_last_name = len(clear_last_name)
print(length_last_name)

username = clear_first_name[0:3] + clear_last_name[0:3] + str(length_first_name)
print(username)

print(f'your assigned username is {username} enjoy the vibe')
