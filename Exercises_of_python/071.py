# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
# e o programa vai informar quantas células de cada valor serão entregues.
# Obs.: Considere que o caixa possui célular de R$50, R$20, R$10 e R$1.

print('='*60)
print('Caixa Eletrônico'.center(60))
print('='*60)
print('-'*60)
print('Bem vindo ao caixa eletrônico Pobre Nunca Mais Rico SEMPRE'.center(60))
print('-'*60)
notas = [50,20,10,1]
while True:
    valor = int(input('Qual valor deseja sacar? '))
    for i in range(0,4):
        cel = valor // notas[i]
        valor = valor%notas[i]
        if cel > 0:
            print(f'Total de {cel} cédulas de R${notas[i]}')
    print('-'*60)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja fazer outro saque? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Obrigado por usar nossa empresa PNMRS.')
    