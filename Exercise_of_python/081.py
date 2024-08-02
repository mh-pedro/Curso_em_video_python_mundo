# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

print('='*60)
print('Construindo listas'.center(60))
print('='*60)

valores = []
resp = ''
while resp in 'Ss':
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if resp == 'Nn':
        break
print(f'Foram digitados {len(valores)} valores.')
print(f'A lista em ordem decrescente é {sorted(valores,reverse=True)}.')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')