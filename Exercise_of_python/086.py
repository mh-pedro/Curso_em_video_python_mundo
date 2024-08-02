# Make a program that can do a matrix of 3x3 dimension and fill in by values 
# read from keyboard.

print('='*60)
print('Matrix of 3x3 dimension'.center(60))
print('='*60)

line = list()
matrix = list()

for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Write the numbers for {[l,c]}: '))
        line.append(n)
    matrix.append(line[:])
    line.clear()
print('='*60)
for l in range(0,3):  
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end=' ')
    print()


