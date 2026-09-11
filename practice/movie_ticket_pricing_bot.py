# this focus on : Functions, Numbers, Arithmetic, Conditionals and String Interpolation (f-string).

def calculate_ticket(age, is_student):
    price = 120

    if age <5 :
        price = 0.00
    elif age >5 or age < 65 :

        price -= 60.0
    elif age > 65:
        price -=70.0
    else:
        print('Invalid age number')
    return f'Your Total Is {price:.2f} Enjoy your Movie'

print(calculate_ticket(10, False))
print(calculate_ticket(4, False))
print(calculate_ticket(40,False))
print(calculate_ticket(68, True))
print(calculate_ticket(10, True))