# Make a program that has a function namely count(), that recive tree parameters: start, end, step. And doing the count. 

import time 

def count(a, b, c):
    print('-'*30)
    if c < 0:
        c = -c
    if c == 0:
        c = 1
    print(f'Count of {a} until {b} from {c} to {c}.')
    if a < b:
        for i in range(a, b, c):
            print(f'{i}', end=' ',flush=True) # We need the value flush=True to print with time
            time.sleep(.5)  
        print('Fim!')
    else:
        for i in range(a, b, -c):
            print(f'{i}', end=' ',flush=True)
            time.sleep(.5)
        print('Fim!')


count(0,10,1)
count(10,0,1)
print('Now is your time to customize!')
a = int(input('Start: '))
b = int(input('End: '))
c = int(input('Step: '))
count(a,b,c)
    


