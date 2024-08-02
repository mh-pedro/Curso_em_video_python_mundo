# Crie um programa onde usuário digita uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

print('='*60)
print('Analisando uma expressão com parênteses'.center(60))
print('='*60)

exp= str(input('Digite uma expressão: '))
pilha = []
for i in exp:
    if i == '(':
        pilha.append('(') # Adiciona um ( na lista pilha
    elif i== ')': # Se tiver um ) ele remover um (
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')