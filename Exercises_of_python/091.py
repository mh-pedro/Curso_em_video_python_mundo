# Make a program where 4 players can use a dice and have random results. Save the results to a dictionary.
# At the end, put the dictionary in order.

from random import randint
import time

players = dict()

print('='*50)
print('Dice players'.center(50))
print('='*50)
cont = 0
for i in range(1,5):
    player_value = int(randint(0,7))
    players[f'player{i}'] = {'value':player_value}
    time.sleep(2)
    print(f'The player {i}) toke {player_value}.')
print('='*50)
sorted_players = sorted(players.items(), key=lambda item: item[1]['value'], reverse=True)

for position, (player, info) in enumerate(sorted_players, start=1):
    print(f'Position {position}: {player} with value {info["value"]}')
    time.sleep(2)
print('='*50)
