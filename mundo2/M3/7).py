count = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):    #Repetição de 1 ao número que foi escolhido
    if num % i == 0: #Se o numero digitado for divisivel pelo contador (O contador vai de 1 ao número que foi escolhido, se o num escolhido for 3: o i vai de 1 a 3), vai adicionar mais um no contador
        count += 1
if count == 2:     #Se o contador for igual a dois, significa que o dentre todas as possibilidades do laço de repetição, o número só foi divisivel por 1 e por ele mesmo
    print(f'{num} É primo')
else:
    print(f'{num} Não é primo')