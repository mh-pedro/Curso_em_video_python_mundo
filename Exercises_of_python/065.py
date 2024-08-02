# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve perguntar
# se ele quer ou não continuar a digitar valores.

print('='*60)
print('Leitura de números'.center(60))
print('='*60)

list = []
s = 0
maior = 0
menor = 0
resp = ''
cont = 0
while resp != 'n':
    n = int(input('Digite alguns números: '))
    resp = str(input('Deseja continuar [s/n]: '))
    list.append(n)
    s = sum(list)
    maior = max(list)
    menor = min(list)
    cont += 1
print('A média entre todos os {} números digitados é {}.\nO maior número foi {} o menor número foi {}.'.format(cont, s/cont, maior, menor))