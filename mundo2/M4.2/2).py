#Passo 1, criar a condição de parada do laço de repetição (A condição de parada é qualquer número negativo) Feito
#Passo 2, fazer com que o programa mostre a tabuada para cada número digitado Feito
while True:
    num = int(input('Digite os números que você quer ver a tabuada de 0 a 10 (Digite algum número negativo caso queira parar): '))
    if num < 0:
        break
    for i in range(0, 11):
        print(f'{num} x {i} = {num * i}')
print('FIM')