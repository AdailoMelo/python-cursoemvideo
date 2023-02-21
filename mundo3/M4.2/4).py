def leiaint(msg):
    n = input(msg)
    while n.isnumeric() != True:
        n = input('Só serão aceitos números inteiros: ')
    return n


num = leiaint('Apenas números: ')
print(f'Você digitou o número {num}')