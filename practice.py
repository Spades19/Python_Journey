# name = "Uriel"
# age = 21

# print(name, type(name))
# print(age, type(age))

# reverse a string
# print(name[::-1])

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('guess num from 1-5 :'))
    if guess != secret_number:
        print('wrong try again!')
        if guess <= 0 or guess >= 5:
            print('guess must be from 1-5')
    else:
        print('Yay you got it !!!')
