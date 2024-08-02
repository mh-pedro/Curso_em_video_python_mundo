#Make a program that reads any angle and displays its sine, cosine and tangent values on the screen.

import math as m
ang = float(input('Write any angle: '))
s = m.sin(m.radians(ang))
c = m.cos(m.radians(ang))
t = m.tan(m.radians(ang))
print('The value of the sin({})={:.1f},cos({})={:.1f},tan({})={}.'.format(ang,s,ang,c,ang,t))