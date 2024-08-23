# Make a program that has a function namely lagger(), that recive any parameters with inter values.
# Your program need to analyse all values and say which then is the large.

import time 
def large(*num):
    cont = lar = 0
    print('Analyse for informed values'.center(50))
    print('-'*50)
    for i in num:
        print(f'{i}', end=' ', flush=True)
        time.sleep(.5)
        if cont == 0: 
            lar = i
        else:
            if i > lar:
                lar = i
        cont += 1        
    print(f'They were informed {len(num)} values.')
    print(f'The large value call was {lar}.')
    print('-='*25)

large()