# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000 reais.
# c) Qual é o nome do produto mais barato.

print('='*60)
print('Lista de Compras'.center(60))
print('='*60)

preco_data = gasto =  cont_mil = ind_min = 0

precos = []
produtos = []

while True:
    prod_data = str(input('Nome do produto: '))
    produtos.append(prod_data)
    preco_data = int(input('Preço do produto: R$'))
    precos.append(preco_data)
    resp = ' '
    while resp in not {SsNn}:
        resp = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
gasto = sum(precos)
for i in range(len(precos)):
    if precos[i] > 1000:
        cont_mil += 1
ind_min = precos.index(min(precos))
prod_min = produtos[ind_min]
print('='*60)
print(f'O total é {gasto}. Temos {cont_mil} custando mais de R$1000 reais. O produto com menor valor é {prod_min}'.center(60))