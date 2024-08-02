# Faça um programa que leia um número qualquer e motre o seu fatorial.

print('='*60)
print('Calculo fatorial de um número com (while)'.center(60))
print('='*60)

n = int(input('Digite um número que deseja calcular o fatorial: '))
res  = 1
cont = 1

while cont <= n:
    res *= cont
    cont += 1
print('\nO resultado de {}! é: {}.'.format(n,res))