# Make a program that read the mane and the grade avarege of a student and saving in a dictionary.
# In the end shows the structure file in the screen. 

student = dict()
print('='*40)
print('Avarege Grade'.center(40))
print('='*40)

student['name'] = str(input('Nome: '))
student['grade'] = float(input(f"The Avarege grade of {student['name']}: "))

if student['grade'] < 7:
    student['situation'] = 'Rejected'
else:
    student['situation'] = 'Approved'
print('-'*40)

for k, v in student.items():
    print(f'- The {k} is equal to {v}')
print('='*40)

