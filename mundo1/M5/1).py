from random import randint
num = randint(0, 5)
chute = int(input("Que número o computador está pensando? (Entre de 1 a 5): "))
if chute == num:
    print(f'Acertou, o número é: {num}')
else:
    print(f'Errou, o número é: {num}')
