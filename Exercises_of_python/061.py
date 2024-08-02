# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão, mas agora usando o (while).

print('='*60)
print('Progressão Aritimetrica'.center(60))
print('='*60)

a1 = int(input('Digite o primeiro termo da Pa: '))
r = int(input('Digite a razão da PA: '))
termo = a1
cont =  1
while cont <= 10:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
print('Fim')