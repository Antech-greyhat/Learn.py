try:
    user_roles = {
    'antony': 'super admin',
    'joshua': 'admin',
    'victoria': 'user'
    }
    name = input('Enter Your Name: ')
    print(f"The role for user {name} is {user_roles[name]}")
except KeyError:
    print("Error: User Not found in the System!")
