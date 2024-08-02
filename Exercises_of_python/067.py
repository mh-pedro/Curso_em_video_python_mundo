# Faça um programa que mostre a tubuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

print('='*60)
print('Tabuada para vários números'.center(60))
print('='*60)

while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    print('-'*60)
    if n < 0:
        break
    for i in range(0,10):
        valor = n * i
        print(f'{valor:3} = {i} x {n}')
    print('-'*60)
print('Fim')
