# Write a program that reads a real number and displays its entire part on the screen
from math import trunc
n = float(input('Write a number: '))
print('Your number is {}, and its entire part is {}.'.format(n, trunc(n)))
