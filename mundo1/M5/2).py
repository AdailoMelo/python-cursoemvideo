#80 km/h velocidade max, multa de 7 reais para cada quilometro acima do permitido.
vel = int(input('Velocidade do carro: '))
if vel > 80:
    print(f'Você ultrapassou a velocidade máxima permitida, multa de: R${(vel - 80) * 7},00')
else:
    print('Parabéns, você dirige como um humano deveria.')