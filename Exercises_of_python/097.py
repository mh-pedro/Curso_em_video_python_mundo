# Make a programa that has a function namely write(), and this function recive any text as a parameter and shows
# a mensagem with adptative length.

def write(txt):
    lenth = len(txt)
    print('~'*(lenth+4))
    print(txt.center(lenth+4))
    print('~'*(lenth+4))

write('Pedro H Morais')

write('Curso em Vídeo')