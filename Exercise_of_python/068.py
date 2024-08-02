# Faça um programa que jogue par ou ímpar com o computador.
# o jogo só será interrompido quando o jogador PERDER, 
# mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

from random import randint, choice

print('='*60)
print('Jogo de par ou ímpar'.center(60))
print('='*60)
lista = ['P', 'I']
soma = cont = 0
while True:
    jogador_num = int(input('Digite um valor entre 1 e 5: '))
    jogador_IP = ' '
    while jogador_IP not in 'PpIi':
        jogador_IP  = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador_num = randint(1,5)
    computador_IP = choice(lista)
    soma = jogador_num + computador_num
    if soma %2 ==0:
        resp = 'P'
    if soma %2 !=0:
        resp = 'I'
    
    if resp == jogador_IP:
        print('-'*60)
        print(f'Você jogou {jogador_num} e o computador {computador_num}. Total de {soma} e deu {resp}.')
        print('-'*60)
        print('Você VENCEU!!!\nVamos Jogar novamente...')
        cont += 1
    if resp != jogador_IP:
        break
    print('='*60)
print('='*60)
print('Você perdeu!!')
print(f'Você ganhou {cont} vezes.')
