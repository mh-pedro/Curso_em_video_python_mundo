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
    person['sexy'] = str(input('Write the sexy:[M/F] '))
    person['age'] = int(input('Write the age: '))
    cont += 1
    people.append(person.copy())
    person.clear()
    ans = str(input('Do you want add more person?[Y/N] ')).strip().lower()[0]
    if ans in 'Nn':
        break
for i in range(0, cont):
    ages += people[i]['age']
    if people[i]['sexy'] in 'Ff':
        wom = people[i]['name']
        womans.append(wom[:])
avarege = ages / cont
for i in range(0, cont):
    if people[i]['age'] >= avarege:
        peo_ave = people[i]['name']
        people_ave.append(peo_ave[:])
print('='*50)
print(f'The total number of registered people were: {cont}')
print('The list of womans are:')
for p, v in enumerate(womans):
    print(f'{p+1}) {v};')
    print()
print('The list of people with age more the age average are:')
for p, v in enumerate(people_ave):
    print(f'{p+1}) {v};')
    print()
print('='*50)
