# Make a program that read the name, sexy and the age for multiple pleople, saving each person in a dict
# and all dict in a list. In the end, shows:
# a) How munch peoples are add.
# b) The average ege of the group.
# c) A list with all woman.
# d) A list with all people with age more the age average of group.

print('='*50)
print('People data'.center(50))
print('='*50)

person = dict()
people = list()
cont = ages = 0
womans = list()
people_ave = list()
while True:
    person['name'] = str(input('Write the name: '))
    while True:
        person['sexy'] = str(input('Write the sexy:[M/F] ')).strip().lower()[0]
        if person['sexy'] in 'MmFf':
            break
        else:
            print('Type again, just type M or F.')
    person['age'] = int(input('Write the age: '))
    cont += 1
    people.append(person.copy())
    person.clear()
    while True:
        ans = str(input('Do you want add more person?[Y/N] ')).strip().lower()[0]
        if ans in 'YyNn' :
            break
        else:
            print('Type again, just type Y or N.')
    if ans in 'Nn':
        break
for i in range(0, cont):
    ages += people[i]['age']
    if people[i]['sexy'] in 'Ff':
        wom = people[i]
        womans.append(wom.copy())
avarege = ages / cont
for i in range(0, cont):
    if people[i]['age'] >= avarege:
        peo_ave = people[i]
        people_ave.append(peo_ave.copy())
print('='*50)
print(f'The total number of registered people were: {cont}')
print(f'The averange age is {avarege:.2f} years.')
print('The list of womans are:')
for i in range(0,len(womans)):
    for k, v in womans[i].items():
        print(f'    {k:<10} = {v:<10};', end=' ')
    print()
print('-'*50)
print('The list of people with age more the age average are:')
for i in range(0,len(people_ave)):
    for k, v in people_ave[i].items():
        print(f'    {k:<10} = {v:<10};', end=' ')
    print()
print('='*50)
