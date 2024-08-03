# Write a program that reads the name of city and tell us if start or not with the name 'Santo'.

n = str(input('Write the name of city: '))
n = n.lower().split()

print("The word 'Santo' appear as the first word in the name of the city? {}.".format('santo' in n[0]))
