# Crie um progama que leia dois valores e mostre um menu na tela:
# - [1] somar
# - [2] multiplicar
# - [3] maior
# - [4] novos números
# - [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

print('='*60)
print('Menu'.center(60))
print('='*60)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digte o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('Escolha uma das opções:\n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair: \n>>>> Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('Soma: {} + {} = {}.'.format(n1,n2,soma))
    elif opcao == 2:
        mul = n1 * n2
        print('Multiplicação: {} * {} = {}.'.format(n1,n2,mul))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior número é {}.'.format(n1,n2,n1))
        else:
            print('Entre {} e {}, o maior número é {}.'.format(n1,n2,n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digte o segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção Inválida. Tente novamente.')
    print('='*60)
print('Você saiu do menu')