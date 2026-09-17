# Task on Dictionary and Dictionary methods.

contact = {
    'name': 'antony',
    'email': 'antony@gmail.com',
    'phone': '0712345678',
    'age': 20
}
print(contact['name'])
print(contact.get('email'))
# trying key that does not exist

#print(contact['address']) #KeyError: 'address'
#print(contact.get('address')) #None

contact.update({'phone': '0712345676'})
contact.update({'address': 40200})
print(contact)

contact.pop('email')
print(contact)

if 'name' in contact:
    print('name is available')
else:
    print('name cannot be found')

contact1 = {'name': 'antony', 'phone': '0743526755'}
contact2 = {'name': 'joshua', 'phone': '0787654332'}
contact3 = {'name': 'eliud', 'phone': '98376342556'}

contacts = ['contact1', 'contact2', 'contact3']
print(contacts)
for contact in contacts:
    print(f"{contact['name']}'s phone is {contact['phone']}")