# Crie um programa que tenha uma tupla com várias palavras
# Depois disso, você deve mostrar, para cada palavra, quais são
# as suas vogais.

pal = ('banana', 'laranja', 'caju', 'morango')

print('='*40)

for i in range(0,len(pal)):
    print(f'\nNa palavra {pal[i].upper()} temos ', end='')
    for letra in pal[i]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


