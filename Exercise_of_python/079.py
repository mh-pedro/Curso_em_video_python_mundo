# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os números
# em ordem crescente.  

print('='*50)
print('Lista de números'.center(50))
print('='*50)

valores = []
resp = ''
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Este valor já foi adicionado')
    resp = str(input('Deseja diginar um novo número? [S/N]')).strip().lower()[0]
    if resp in 'Nn':
        break
print('='*50)
print(f'Os valores digitados foram {sorted(valores)}')