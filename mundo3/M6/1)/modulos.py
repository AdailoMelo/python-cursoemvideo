def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'\033[0;31mErro no valor, só serão aceitos números inteiros.\033[m')
        else:
            return num     
def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print(f'\033[0;31mErro no valor digitado, só serão aceito números, e caso sejam inteiros serão transformados em reais.\033[m')
        else:
            return num