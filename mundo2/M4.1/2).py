from random import randint
computador = randint(0, 10)
cont = 0
tentativa = int(input('Tente adivinhar um número entre 0 e 10: '))
while tentativa != computador:
    tentativa = int(input('Errou, tente de novo: '))
    cont += 1
print(f'Acertou, o número é {computador}, você precisou de {cont+1} tentativas para acertar')