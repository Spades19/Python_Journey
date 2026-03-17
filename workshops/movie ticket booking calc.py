base_price = 2500
age = 21

show_time = 'Evening'
seat_type = 'Platinum'

if age >= 18:
    print('user is old enough to book ticket on their own')

if age >= 21:
    print('user is old enough for evening shows')
else:
    print('user is not old enough for these types of shows')

is_member = False
is_weekend = False

discount = 0

# applying disocunt to members
if is_member and age >= 21:
    discount = 3
    print('user eligible for discount')
else:
    print('User does not quality for discount')
print('Discount', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21:
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied ')
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    final_price = base_price + service_charges + extra_charges - discount
    print('Final price of ticket:', final_price)
else:
    service_charges = 1
print('Service charges:', service_charges)
