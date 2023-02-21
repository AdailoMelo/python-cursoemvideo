from random import randint
from time import sleep
def sorteia(n):
    for i in range(0, 5):
        n.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: ', end='')
    for num in n:
        print(num, end=' ', flush=True)
        sleep(0.45)
    print()
def somaPar(l):
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares dentro de {numeros} é igual a: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)
