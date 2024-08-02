# Desenvolva um programa que leia quatro valores pelo tecldo
# e guarde-os em um tupla. No finall, mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais forom os números pares.

n  = (int(input('Digite um número: ')), 
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O valor 9 não foi encontrado.')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3)}')
else:
    print('O valor 3 não foi encontrado')
for i in n:
    if i%2 ==0:
        print('O valors pares digitados foram:',end='')
        print(f'{i}', end=' ')
print('Não foi encontrado valores pares.')