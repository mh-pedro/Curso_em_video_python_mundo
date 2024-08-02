# Faça um programa que leia um número qualquer e motre o seu fatorial.

print('='*60)
print('Calculo fatorial de um número com (while)'.center(60))
print('='*60)

n = int(input('Digite um número que deseja calcular o fatorial: '))
c = n
f = 1

print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end ='')
    f *= c
    c -= 1
print('{}'.format(f))