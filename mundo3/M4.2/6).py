C = ('\033[m', 
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(C[cor])
    print('~'*tam)
    print(msg)
    print('~'*tam)
    print(C[0])

def ajuda(com):
    titulo(f'  Acessando o manual do comando \'{com}\'', 4)
    print(C[6], end='')
    help(com)
    print(C[0], end='')

comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou bibilioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  Até logo', 1)