primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
verifica = 1
while verifica != 0:
    while cont != 10:
        print(f'{primeiro} =>', end=' ')
        primeiro += razao
        cont += 1
    verifica = int(input('Quantos termos a mais você deseja?: '))
    cont -= verifica
print('FIM')
