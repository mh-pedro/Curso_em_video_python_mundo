# Crie uma programa que vai ler vários números e colcoar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares, respectivamente.
# Ao final, mostre os conteúdos das três listas geradas.

print('='*60)
print('Separando pares e impares de uma lista'.center(60))
print('='*60)

lista = []
par = []
impar = []

resp = ''
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n%2 == 0:
        par.append(n)
        print(f'O número {n} é par e foi adicionado na lista pares')
    else:
        impar.append(n)
        print(f'O número {n} é impar e foi adicionado na lista ímpares')      
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if resp == 'Nn':
        break
print('='*60)
print(f'Os valores digitados foram {lista}.')
print(f'Sendo {par} os valores pares.')
print(f'Sendo {impar} os valores ímpares.')

