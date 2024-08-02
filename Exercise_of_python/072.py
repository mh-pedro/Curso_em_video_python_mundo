# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, do zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('='*60)
print('Leitura de números')

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

resp = ' '
while resp not in 'Nn':
    while True:
        n = int(input('Digte um número: '))
        if 0 <= n <= 10:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {num[n]}')
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Obrigado')