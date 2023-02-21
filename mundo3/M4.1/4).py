from random import randint
from time import sleep

def maior(l):
    print('Analisando os valores passados...')
    for i in l:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(l)}')
    print('-='*20)
lista = []
quantidade = randint(1, 15)
for valores in range(1, quantidade+1):
    lista.append(randint(1, 10))
print('-='*20)
maior(lista)