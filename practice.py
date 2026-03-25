# name = "Uriel"
# age = 21

# print(name, type(name))
# print(age, type(age))

# reverse a string
# print(name[::-1])

# secret_number = 3
# guess = 0

# while guess != secret_number:
# guess = int(input('guess num from 1-5 :'))
# if guess != secret_number:
# print('wrong try again!')
# if guess <= 0 or guess >= 5:
# print('guess must be from 1-5')
# if guess == 2:
# break
# else:
# print('Yay you got it !!!')


numbers = [' spanish', ' english', ' japanese', ' mongolian']
ids = [1, 2, 3, 4]
# index = 0
# print(list(zip(numbers, ids)))
# for number in numbers:
#  print(f'index{index} and number{number}')
# index += 1
# print(list(enumerate(numbers)))

# for index, number in enumerate(numbers):
#   print(f'Index{index} and number{number}')
for name, id in zip(numbers, ids):
    print(f'Lang: {name}')
    print(f'ID: {id}')
