# Escreva um programa que leia 5 valores númericos e
# guarde-os em uma lista.
# No final, mostre qual foi o maiore o menor valor digitado
# e suas respectivas posições na lista.

print('='*40)
print('Leitura de valroes com o uso de lista'.center(40))
print('='*40)

maior = 0
menor = 0
valores = []
for cont in range(0,4):
    valores.append(int(input(f'Digite um valor para posição [{cont}]: ')))
    if cont == 0:
        menor = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Os valores digitados foram: {valores}.')
print(f'O maior valor digitado foi {maior}. Na posição ',end='')
for i, v in enumerate(valores):
    if v == maior:
            print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi  {menor}. Na posição ', end='')
for i, v in enumerate(valores):
     if v == menor:
          print(f'{i}...',end='')
print()