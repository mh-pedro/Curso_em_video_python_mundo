# Make a program that reads the length of opposite cathetus and adjacent cathetus of a triangle, and calculate the length of hypotenuse.

c1 = int(input('Write the opposite cathetus of a triangle: '))
c2 = int(input('Write the adjacent cathetus of a triangle: '))
hy = (c1**2+c2**2)**(1/2)

print('The opposite cathetus is {}, the adjacent cathetus is {} and the hypotenuse is {:.2f}.'.format(c1,c2,hy))
