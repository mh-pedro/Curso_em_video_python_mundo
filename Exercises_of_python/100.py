# Make a program that has a list namely number and two functions namely choose() and sumEven().
# The first fuction will choose 5 numbers and puting inside of the list and the second function will show the sum for all even numbers.

from random import randint
import time
def choose(lst):
    print('The 5 values are choose for list: ', end=' ')
    for i in range(0,5):
        n =randint(0,10)
        lst.append(n)
        print(f'{n}', end=' ',flush=True)
        time.sleep(0.3)
    print('FINISH!')
    
def sumEven(lst):
    sum = 0
    for i in lst:
        if i % 2==0:
            sum += i
    print(f'The sum of even values of {lst} are {sum}.')

num = list()
choose(num)
sumEven(num)