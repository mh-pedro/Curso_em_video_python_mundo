# Make a program that has a function namely area(), and this function recive the dismensions of a 
# rectangular land (width and length) and show the value of the land area.

def area(a, b):
    area = a * b
    print(f"The area of rectangular land {a}x{b} is {area} m\u00B2.")

print('Land Control'.center(30))
print('-'*30)
a = float(input('WIDTH (m): '))
b = float(input('LENGTH (m): '))
area(a, b)