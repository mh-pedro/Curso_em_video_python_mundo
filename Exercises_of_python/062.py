# Melhore o DESAFIO 061 perguntando para o usúario se ele quer mostar mais alguns termos. 
# O programa encerra quando ele disser que quer mostrar 0 termos. 
print('='*60)
print('Progressão Aritimetrica'.center(60))
print('='*60)

a1 = int(input('Digite o primeiro termo da Pa: '))
r = int(input('Digite a razão da PA: '))
termo = a1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
    print('Pausa')
    mais = int(input('Digite qanto mais números quer ver: '))
print('Foram apresentados {} números da PA'.format(total))