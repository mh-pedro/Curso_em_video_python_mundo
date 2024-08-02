# Make a program where the user write seven numerical values
# and he adds in one list, but keep separate between odd and even.
# In the end, shows the odd and even in crescent order.

print('='*60)
print('List of odd and even numbers'.center(60))
print('='*60)

odd = list()
even = list()
numbers = [odd,even]
# numbers = [[],[]]

for i in range(0,8):
    n = int(input(f'Write the {i+1}) number: '))
    numbers.append(n)
    if n%2 == 0:
        odd.append(n)
        #numbers[0].append(n)
    else:
        even.append(n)
        #numbers[1].append(n)
print('='*60)
print(f'The list of number is {sorted(numbers)}.')
print(f'The odd numbers are {sorted(numbers[0])}.')
print(f'The even numbers are {sorted(numbers[1])}.')
