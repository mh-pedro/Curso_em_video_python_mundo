## D058
# Melhore o jogo do D028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acetar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random
print('='*60)
print('Jogo de adivinhação'.center(60))
print('='*60)

computador = random.randint(1,6)
n = 0
cont = 0
while n != computador:
    n = int(input('Digte um número: '))
    cont += 1
print('Você precisou de {} rodadas para acertar o número {} que o computador pensou.'.format(cont,n))