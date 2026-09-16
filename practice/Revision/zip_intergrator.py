usernames = ['antech_admin', 'dev_guest', 'sys_monitor']
clearances = ['Superuser', 'Read-Only', 'Auditor']

for user,clearance in zip(usernames,clearances):
    print(f'Account {user} is assigned {clearance} clearance.')

developers = ['antony', 'joshua', 'eliud']
roles = ['Backend Developer', 'UI/UX Designer', 'Frontend Developer']

for developer,role in zip(developers,roles):
    print(f'{developer} is assigned the role {role}.')