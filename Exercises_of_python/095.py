# Enhance the chalenge 093 that then works with many players. Add a visulation system that explit 
# the use of each player


print('='*50)
print('Table of football player'.center(50))
print('='*50)

players = list()

while True:
    player = {}
    gols = []
    player['name'] = str(input('Name of football player: '))
    player['games'] = int(input(f"How munch games {player['name']} played? "))

    for i in range(0,player['games']):
        gol = int(input(f"How many goals in game {i+1}: "))
        gols.append(gol)

    player['gols'] = gols[:]
    player['total_gols'] = sum(gols)
    players.append(player.copy())
    player.clear()
    gols.clear()

    ans = str(input('Do you want add other player?[Y/N]: ')).strip().lower()[0]
    if ans in 'Nn':
        break
    
print('='*50)
print(f'{"Cod":<5}{"Name":<15}{"games":<10}{"gols":<10}{"Total":<}')
print('-'*50)

for idx, player in enumerate(players):
    print(f"{idx:<5}{player['name']:<15}{str(player['gols']):<20}{player['total_gols']:<5}")
print('-'*50)
while True:
    show_player = int(input("Show which player's data? (999 to stop): "))
    if show_player == 999:
        break
    else:
        print(f"The data for {players[show_player]['name'].upper()}:")
        for p, v in enumerate(players[show_player]['gols']):
            print(f'No game {p+1} he made {v} gols.')
        print('-'*50)
print('Thanks!!')
