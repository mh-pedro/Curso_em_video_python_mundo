# Make a program that can manage the utilization of a football player. The program can be read the name of player,
# and how munch game he played. After, the program will read the number of gols for each game. In the end, every thing will be save in a dict, including total goals

print('='*50)
print('Table of football player'.center(50))
print('='*50)

player = dict()
gols = list()

player['name'] = str(input('Name of football player: '))
player['games'] = int(input(f"How munch games {player['name']} played? "))
for i in range(0,player['games']):
    gol = int(input(f"How munc gols in the game {i}: "))
    gols.append(gol)
player['gols'] = gols
player['total_gols'] = sum(gols)
print('='*50)
for k, v in player.items():
    print(f"The fild {k.upper()} has the value {v}.")
print('='*50)
print(f"The player {player['name']} played {player['games']} match.")
for p, v in enumerate(player['gols']):  
    print(f"    => In the game {p}, he made {player['gols'][v]} gols.")
print(f"The total gols are {player['total_gols']}")
print('='*50)
