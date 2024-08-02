# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Apenas os 5 primeiros colcoados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time do Flamengo.

tabela = ('Flamengo', 'Botafogo', 'Palmeiras', 'São Paulo', 'Bahia', 'Atletico-PR', 'Cruzeiro', 'Fortaleza','Bragatino', 'Internacional', 'Juventude', 'Atlético-MG', 'Vasco', 'Criciúma', 'Vitória', 'Cuibá', 'Corinthians', 'Grêmio', 'Atlético Goianiense', 'Fluminense')

print('='*60)
print('Informações sobre os times da CBF'.center(60))
print('='*60)

print(f'Os cinco primeiros classificados da CBF são:')
for i in range(0,5):
    print(f'{i+1}) {tabela[i]}')
print('-'*60)
print(f'Os quatro ultimos classificados da CBF são:')
for i in range(19, 14, -1):
     print(f'{i+1}) {tabela[i]}')
print('-'*60)
print(f'Lista com os times em ordem alfabética')
for i in range(0,19):
    print(sorted(tabela)[i])
print('-'*60)
print(f'Posição de um time')
pos = tabela.index('Flamengo')
print(f'O time Flamengo se encontra na posição {1+pos})')
