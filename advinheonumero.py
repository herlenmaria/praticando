from random import randint
computador = randint(0,10)
jogador=0 #acertou=False
n=0
print('Vamos brincar!!! Vou pensar em um número entre 1 a 10 e você vai tentar acertar!!')
while computador != jogador: #while not acertou:
    jogador=int(input('Em que número eu pensei 0 a 10: '))
    n+=1
    if computador == jogador:
        print('\033[35mACERTOOOU! Na {}° vez!'.format(n))
        #acertou = True
    else:
        if jogador > computador:
            print('\033[33mMenos... Tenta novamente!\033[m')
        elif computador > jogador:
            print('\033[33mMais...Tenta novamente!\033[m')