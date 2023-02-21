def aumentar(num, porcentagem = 0, format = False, simbolo = 'R$'):
    aumento = num * (1 + (porcentagem / 100))
    if format == False:
        return aumento
    else:
        return moeda(aumento, simbolo)
def diminuir(num, porcentagem = 0, format = False, simbolo = 'RS'):
    reducao = num * (1 - (porcentagem / 100))
    if format == False:
        return reducao
    else:
        return moeda(reducao, simbolo)
def dobro(num=0, format = False, simbolo = 'RS'):
    num *= 2
    if format == False:
        return num
    else:
        return moeda(num, simbolo)
def metade(num=0, format = False, simbolo = 'RS'):
    num /= 2
    if format == False:
        return num
    else:
        return moeda(num, simbolo)
def moeda(preco = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
