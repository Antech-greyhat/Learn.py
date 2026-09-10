base_price = 15
age = 21
seat_type = "Gold"
show_time = 'Evening'

if age > 17:
    print('User Is Eligible To Book  A Movie Ticket')
if age >= 21:
    print('User Is Eligible For Evening Movie')
else:
    print('User Is Not Eligible For Evening Show')
is_member = True
is_weekend = False
discount = 0

if is_member:
    discount = 3
    print('User Qualifies For The Membership Discount')
else:
    print('User Does Not Qualify For Membership Discount')
print("Awarded Discount is:", discount)

# using the and operator to compare 2 conditions if is member and age.
if is_member and age >= 21:
    discount = 3
    print("User Qualifies For The Membership Discount")
else:
    print("User Does Not Qualify For The Membership Discount")
print('Discount is:', discount)

#Note: if you change the value of is_member to False then the discount will be 0

extra_charges = 0

if is_weekend:
    extra_charges = 5
    print('Extra Charges Will Be Applied')
else:
    print('No Extra Charges Will be Applied') # this applies id is_weekend is True
print("Extra Charges:", extra_charges)

# using the or operator which checks atleast one of the two condition is true

if is_weekend or show_time == 'Evening':
    extra_charges = 5
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

if age >= 21:
    print('Ticket Booking Conditions Have Passed')
else:
    print('Ticket Booking Denied Due to Restrictions On the Age')

# using both or operator with the and operator.

if age >= 21 or age >= 18 and show_time != 'Evening':
    print('Ticket booking passed')
else:
    print('Ticket booking failed try again after passing the conditions')

# When multiple logical operators are used in an if statement, conditions joined with and are evaluated before conditions joined with or.
# Parentheses () are used in Python to group conditions and control the order in which they are evaluated.

if age >=21 or age >= 18 and (is_member or show_time != 'Evening'):
    print('Can book a ticket now')

    # using nested if which allows you to check for additional condition if the first one has been satisfied
    # using if...elif...else which checks multiple condition in order
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 10
    elif seat_type == 'Gold':
        service_charges = 5
    else:
        service_charges = 1
    print('Service Charges:', service_charges)
    final_price = base_price + service_charges + extra_charges - discount
    print("Final Booking Price Is:", final_price) #output : 22
else:
    print('cannot a book a ticket')

# clean syntax of the if...elif...else :
#if condition1:
   # Code to execute if condition1 is True
#elif condition2:
   # Code to execute if condition1 is False and condition2 is True
#else:
   # Code to execute if all conditions are False