# Make a program that read the mane and the grade avarege of a student and saving in a dictionary.
# In the end shows the structure file in the screen. 

student = dict()
print('='*40)
print('Avarege Grade'.center(40))
print('='*40)
student['name'] = str(input('Nome: '))
student['grade'] = float(input(f"The Avarege grade of {student['name']}: "))

print(f"The name is equal to {student['name']}.")
print(f"The avarege grade is equal to {student['grade']}.")
if student['grade'] < 7:
    print('The student is rejected.')
else:
    print('The student is approved.')
print('='*40)

