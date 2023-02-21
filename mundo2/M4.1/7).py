cont = 0
primeiro = 0 
segundo = 1
quantidade = int(input('quantos termos você quer ver?: '))
while cont != quantidade:
    print(f'{primeiro} =>', end=' ')
    prox = primeiro + segundo
    primeiro = segundo
    segundo = prox
    cont += 1
print('FIM')