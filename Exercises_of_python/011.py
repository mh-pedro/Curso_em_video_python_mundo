# Make a program that reads the width and height of the wall in meters, calculates its area and the amount of paint needed to draw, take into account that for each liter of paint we can paint an area of 2m^2.

n1 = int(input('Enter the width of the wall in meters: '))
n2 = int(input('Enter the hight of the wall in meters: '))
a = n1*n2
n3 = a/2

print('Your wall has {}m\u00b2 and you need {}L of paint.'.format(a,n3))

