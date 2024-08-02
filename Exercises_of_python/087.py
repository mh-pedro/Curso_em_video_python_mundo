# Improve the previous chalenge, shows in the end:
# a) The sum of all odd values written.
# b) The sum of the third column
# c) The biggest value in the second line.

print('='*60)
print('Matrix of 3x3 dimension'.center(60))
print('='*60)

line = list()
matrix = list()
sum_odd = sum_3l = sum_3c = bigger = 0
for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Write the numbers for {[l,c]}: '))
        ###### This part is the upgrad ####
        if n%2 == 0:
            sum_odd += n
        if c == 2:
            sum_3l += n
        if c == 1:
            if c == 0:
                bigger = n
            else:
                if n > bigger:
                    bigger = n
        ###################################
        line.append(n)
    matrix.append(line[:])
    line.clear()
print('='*60)
for l in range(0,3):  
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end=' ')
    print()
print('='*60)
print(f'The sum of all values odd is {sum_odd}.')
print(f'The sum of values of third column is {sum_3l}.')
print(f'The biggest values of second line is {bigger}.')
