from random import randint
from time import sleep
dados = []
jogos = []
palpites = int(input('Quantos jogos serão gerados? '))
for i in range(0 , palpites):
    for jogo in range(0, 6):
        dados.append(randint(1, 60))
    jogos.append(dados[:])
    dados.clear()
for i in jogos:
    print(i)
    sleep(1.5)
