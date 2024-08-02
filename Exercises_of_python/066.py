# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos
# números foram digitados e qual foi a soma entre eles
# desconsiderando o 999.

print('='*60)
print('Leitura de vários números com o uso do Break'.center(60))
print('='*60)

n = soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} número e a soma entre eles é {soma}')