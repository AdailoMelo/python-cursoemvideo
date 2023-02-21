lista = []
listap = []
listai = []
while True:
    valor = int(input('Digite o valor desejado: '))
    lista.append(valor)
    if valor % 2 == 0:
        listap.append(valor)
    else:
        listai.append(valor)
    continuar = input('Quer digitar outro valor?: ').strip().upper()[0]
    while continuar not in ('N', 'S'):
        continuar = input('Não entendi o que você quis dizer, digite sim ou não: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'A lista completa: {lista}', end=' ')
print(f'Números pares: {listap}', end=' ')
print(f'Números ímpares: {listai}')
lista.sort()
print(f'Em ordem: {lista}')