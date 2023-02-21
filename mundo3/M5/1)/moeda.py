def aumentar(num, porcentagem = 10):
    aumento = num * (1 + (porcentagem / 100))
    return aumento
def diminuir(num, porcentagem = 10):
    reducao = num * (1 - (porcentagem / 100))
    return reducao
def dobro(num=0):
    num *= 2
    return num
def metade(num=0):
    num /= 2
    return num

