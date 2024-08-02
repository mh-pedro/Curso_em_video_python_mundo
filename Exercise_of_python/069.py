# Crie um programa que liea a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

idades = []
sexos = []

cont_18 = cont_20M = cont_H = 0
resp = ' '
while True:
    if resp != 'N':
        print('Cadastre uma pessoa')
        idade_dada = int(input('Idade: '))
        idades.append(idade_dada)
        sexo_dada = ' '
        while sexo_dada not in 'MmFf':
            sexo_dada  = str(input('Sexo: ')).strip().upper()[0]
        sexos.append(sexo_dada)
    else:
        break
    print('-'*60)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    print('-'*60)
for i in range(len(idades)):
    if idades[i] > 18:
        cont_18 +=1
    if sexos[i] == 'F' and idades[i] <= 20:
        cont_20M +=1
    if sexos[i] == 'M':
        cont_H +=1
        
if cont_18 == 1:
    sing_plu_18 = 'Foi cadastrado 1 pessoa'
else:
    sing_plu_18 = f'Foram cadastrados {cont_18} pessoas'
if cont_H == 1:
    sing_plu_H = '1 homem foi cadastrado'
else:
    sing_plu_H = f'{cont_H} homens foram cadastrados'
if cont_20M == 1:
    sing_plu_20M = '1 mulher foi cadastrada'
else:
    sing_plu_20M = f'{cont_20M} mulheres com menos de 20 foram cadastradas.'

print(f'{sing_plu_18} com mais de 18 anos.\n{sing_plu_H}.\n{sing_plu_20M}')
print('='*60)
print('O cadastro terminou')