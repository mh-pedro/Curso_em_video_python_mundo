# Make a program that help a player of MEGA SENA to do some "palpites".
# The program will ask how munch games, the play would be do and the progama
# will sorted 6 numbers
# between 1 and 60 for each game, add then in a list. 


print('='*60)
print('The MegaSena Game'.center(60))
print('='*60)
from random import randint
import time

ticket = list()
game = list()
numbers = 0
while True:
    n = int(input('Write the numbers of the game you want: '))
    for gam in range(0,n):
        for i in range(0,7):
                while numbers in game:
                    numbers = randint(1,61)
                game.append(numbers)
        ticket.append(game[:])
        game.clear()
    print('='*60)
    print('Drawing the games'.center(60))
    print()
    for i in range(0,n):
        print(f'The game {i+1}): {sorted(ticket[i])}')
        time.sleep(1)
    print('='*60)
    answer = ' '
    while answer not in 'YyNn':
        answer = str(input('Do you want new numbers? [Y/N]')).strip().lower()[0]
    if answer in 'Nn':
        break
    print('='*60)
print('='*60)
print('Thanks for use us and < GOOD LUCK! >')
    

