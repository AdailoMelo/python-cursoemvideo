def linha():
    return '-' * 42
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'\033[0;31mErro no valor, só serão aceitos números inteiros.\033[m')
        else:
            return num  
def menu(lista):
    from time import sleep
    from lib.Arquivo import lerArquivo, Cadastrar
    while True:
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        for pos, i in enumerate(lista):
            print(f'\033[0;33m{pos+1} - \033[m', end='')
            print(f'\033[34m{i}\033[m')
        print(linha())
        n = leiaInt('\033[0;33mSua Escolha: \033[m')
        if n == 1:
            print(linha())
            print('OPÇÃO 1'.center(42))
            print(linha())
            lerArquivo('cursoemvideo.txt')
            sleep(1.5)
            
        elif n == 2:
            print(linha())
            print('OPÇÃO 2'.center(42))
            print(linha())
            Cadastrar('cursoemvideo.txt')
            sleep(1.5)
        elif n == 3:
            print(linha())
            print('FIM DO SISTEMA, VOLTE SEMPRE!'.center(42))
            print(linha())
            break
        else:
            print(f'\033[0;31mErro! Por favor, digite 1, 2 ou 3\033[m')
            sleep(1.5)           