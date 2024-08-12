# Make a program where 4 players can use a dice and have random results. Save the results to a dictionary.
# At the end, put the dictionary in order.

from random import randint
import time
from operator import itemgetter
players = dict()

print('='*50)
print('Dice players'.center(50))
print('='*50)

for i in range(1,5):
    player_value = int(randint(1,7))
    players[f'player{i}'] = player_value
    time.sleep(2)
    print(f'The player {i}) toke {player_value}.')
print('='*50)

sorted_players = dict()
# The key = itemgetter(1) getter the item in position 1 from de dict
sorted_players = sorted(players.items(), key=itemgetter(1), reverse=True)
# the results after sorted is a list with tuple. 

for position, player in enumerate(sorted_players, start=1):
    print(f'Position {position}: {player[0]} with value {player[1]}.')
    time.sleep(2)
print('='*50)
