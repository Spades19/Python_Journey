first_name = 'Mark'
last_name = 'Moore'
print(first_name)
print(last_name)

full_name = first_name + ' ' + last_name
print(full_name)

address = '235 Side Street'
print(address)

address += ' Apartment 3B'
print(address)

employee_age = 25
employee_info = full_name + ' is ' + str(employee_age)

print(employee_info)


experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Backend Web developer'
salary = 80000
# using f strings
# use only 1 f at the begining
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: {salary}'
print(employee_card)

# slicing strings
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)


last_three = employee_code[-3:]  # print last three indexes
print(last_three)
