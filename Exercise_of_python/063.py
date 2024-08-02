# Escreva um programa que leina um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequência de Fibonacci.
print('='*60)
print('Sequência de Fibonacci'.center(60))
print('='*60)

n = int(input('Quantos elementos deseja ver? '))
cont = 1
t1 = 0
t2 = 1
t3 = t2 + t1
print('{} -> {} ->'.format(t1,t2), end='')
while cont <= n:
    t1 = t2
    t2 = t3
    t3 = t2 + t1
    print('{} -> '.format(t3), end='')
    cont += 1
print('Fim')

