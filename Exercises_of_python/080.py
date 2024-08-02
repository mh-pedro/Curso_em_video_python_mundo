# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção. (sem usar o sort())
# No final, mostre a lista ordenada na tela.

print('='*50)
print('Cadastrando números numa lista'.center(50))
print('='*50)

valores = []
for i in range(0,5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
                if num <= valores[pos]:
                    valores.insert(pos,num)
                    print(f'O valor {num} foi adicionado na posição {pos}.')
                    break
                pos += 1
print(valores)
