## D058
# Melhore o jogo do D028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acetar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('='*60)
print('Jogo de adivinhação'.center(60))
print('='*60)

computador = randint(1,10)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Tente adivinhar: '))
    if jogador == computador:
        acertou = True
    else:  
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
    cont += 1
print('Você precisou de {} rodadas para acertar o número {} que o computador pensou.'.format(cont,computador))