# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequencia. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

lista = ('carne',5,
        'feijão',3,
        'arroz',2,
        'nutela',10)

print('='*40)
print('Lista de compras'.center(40))
print('-'*40)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('='*40)