# focus string methods: (strip, lower), string slicing and type checking (isinstance)

def setup_profile(full_name, birth_year):
    if not isinstance(birth_year, int):
        return 'Invalid Year of birth'
    clean_name = full_name.strip()
    lower_name = clean_name.lower()
    username = lower_name[0:3]
    email_name = username.replace(" ", ".")
    email = email_name + "@company.com"
    return f'your username is: {username} and your email is: {email}'

print(setup_profile('kate', '2000'))
print(setup_profile('antony', 2004))
print(setup_profile('mwendwa', 1990))
print(setup_profile('kimjong', 2000))
print(setup_profile('antonymwendwa', 6790))