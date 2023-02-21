primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont != 10:
    print(f'{primeiro} =>', end=' ')
    primeiro += razao
    cont += 1
print('FIM')