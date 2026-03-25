odd_number = []

for num in range(25):
    if num % 2 != 0:
        odd_number.append(num)

print(odd_number)

# shorter way using list comprehension

odd_number = [num for num in range(25) if num % 2 != 0]
print(odd_number)
