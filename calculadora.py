c = ('\033[m',     #0-sem cor
     '\033[0;31m', #1-vermelho
     '\033[0;32m', #2-verde
     '\033[0;33m', #3-amarelo
     '\033[0;34m', #4-azul
     '\033[0;35m', #5-roxo
     )

def isFloat(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except(ValueError,TypeError):
            print(f'{c[1]}ERRO! Digite um número válido!{c[0]}')


def verif_op(msg):
    while True:
        operador = str(input(msg))
        if operador in '+-*/0':
            return operador
        else:
            print(f'{c[1]}ERRO! Digite um operador válido!{c[0]}')

def operacao(operador):
    if operador == '-':
        return f'{c[3]}{x} - {y} = {x-y}{c[0]}'
    if operador == '+':
        return f'{c[3]}{x} + {y} = {x+y}{c[0]}'
    if operador == '*':
        return f'{c[3]}{x} * {y} = {x*y}{c[0]}'
    if operador == '/':
        return f'{c[3]}{x} / {y} = {x/y}{c[0]}'

#PROGRAMA PRINCIPAL

finalizar = 'snNS'
while finalizar != 'N':
    operador = verif_op(f'SOMA [{c[3]}+{c[0]}]\n'
                 f'SUBTRAÇÃO [{c[3]}-{c[0]}]\n'
                 f'MULTIPLICAÇÃO [{c[3]}+{c[0]}]\n'
                 f'DIVISÃO [{c[3]}/{c[0]}]\n'
                 'Digite a operação desejada: ')
    x = isFloat(f'Digite a {c[5]}primeira {c[0]} varíável: ',)
    y = isFloat(f'Digite a {c[4]} segunda {c[0]} variável: ')
    print(f'=*' * 20)
    print(operacao(operador))
    print(f'=*' * 20)
    finalizar = input('Deseja continuar (S/N): ').upper()
    print(f'=*' * 20)
print('VOLTE SEMPRE!')