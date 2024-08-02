# Write a program that reads the name of person and show:
# - The name with all letters capitalize
# - The name with all letters low
# - Count the letters with not the spaces
# - Count the letters in the first name

name = 'Pedro Henrique Morais'
n1 = name.upper()
n2 = name.lower()
n3 = len(name.lstrip())
n4 = len(name.split()[0])

print('The name Pedro Henrique Morais, can be write in upper forme like ({}) or lower forme like ({}), has ({}) letters and the first name has ({}) letters.'.format(n1,n2,n3,n4))
