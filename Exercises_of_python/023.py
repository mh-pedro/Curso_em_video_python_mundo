# Write a program that reads a number of 0 to 9999 and show in the screen each number separeted

n = int(input("Write a number between 0 and 9999: "))
print('The number is ({}), and we has \nUnit = {} \nTen = {} \nHundred = {} \nThousands = {}.'.format(n,n // 1 % 10,n // 10 % 10,n // 100 % 10,n // 1000 % 10))