### D057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('='*60)
print('Leitura do sexo de uma pessoa'.center(60))
print('='*60)

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))