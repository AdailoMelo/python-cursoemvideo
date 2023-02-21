from random import randint
from time import sleep
from operator import itemgetter   #Estudar esse itemggetter
jogadores = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4':randint(1,6)}
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)   #Entender o que essa linha faz, e o raciocinio por trás do programa
print(ranking)
print(f'{"-="*30}\n== Ranking dos jogadores ==')
cont=1
for pos, i in enumerate(ranking):
    print(f'Na posição {pos+1}: {i[0]} com {i[1]} pontos no dado')
    sleep(1)