# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma lista com as pesadas. 
# c) Uma listagem com as pessoas mais leves.

print('='*60)
print('List of names and weight'.center(60))
print('='*60)

peoples = list()
data = list()
weight_plus = list()
weight_less = list()

contp = sum_weight = 0  

while True:
    name = str(input('Name: '))
    contp +=1
    weight = float(input('Weight: '))
    data.append(name)
    data.append(weight)
    peoples.append(data[:])
    data.clear()
    answer = ' '
    while answer not in 'NnYy':
        answer = str(input('Do you wish to continue? [Y/N] ')).strip().lower()[0]
    if answer in 'Nn':
        break
for p in peoples:
    sum_weight += p[1]
avarege_weight = sum_weight / contp
print(avarege_weight)
for p in peoples:
    if p[1] <= avarege_weight:
        weight_less.append(p)
    elif p[1] > avarege_weight:
        weight_plus.append(p)
print('='*60)
print(f'The {contp} peoples are indexded and the avarege weight is {avarege_weight:.2f} Kg.')
print('-'*60)
print(f'The list of large weight are ')
for p in peoples:
        if p[1] <= avarege_weight:
            print(f'{p[0]} with {p[1]} Kg.',end=' ')
print()
print('-'*60)
print(f'The list of less weight are ')
for p in peoples:
        if p[1] > avarege_weight:
            print(f'{p[0]} with {p[1]} Kg.',end=' ')
        print()
print('='*60)


