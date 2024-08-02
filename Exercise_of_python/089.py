# Make a program that read names and two school grades for several students
# and add all in a list. In the end, shows a grad that contains each averange student grades
# and has a possibility to shows the individual grades.

print('='*60)
print('School Grades'.center(60))
print('='*60)

student = list()
grades = list()
clas = list()
cont_st = grad_student= 0
while True:
    name = str(input('Name: '))
    n1 = float(input('Grade 1: '))
    n2 = float(input('Grade 2: '))
    avarenge = (n1+n2)/2
    cont_st += 1
    student.append(name)
    grades.append(n1)
    grades.append(n2)
    grades.append(avarenge)
    student.append(grades[:])
    clas.append(student[:])
    student.clear()
    grades.clear()
    answer = str(input('Do you want continum? [Y/N]: ')).strip().lower()[0]
    if answer in 'Nn':
        break
print('='*60)
print('No.       Nome           Média')
print('-'*60)
for p, n in enumerate(clas):
    print(f'{p:<10}{n[0]:<15}{n[1][2]:>5}')
print('-'*60)
while grad_student != 999:
    grad_student = int(input('Show the grads to which student? (999 to finish): '))
    if grad_student != 999:
        print(f'The grades for {clas[grad_student][0]} are {clas[grad_student][1][0:2]}.')
        print('-'*60)
    else:
        grad_student = 999
print('Thanks')