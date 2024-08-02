# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).

print('='*60)
print('Leitura de números'.center(60))
print('='*60)

cont =  n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        s+= n
    else:
        n = 999
print('Você digitou {} números e a soma entre eles é {}.'.format(cont,s))
