lista = []
while True:
    value = int(input('Digite um número: '))
    if value not in lista:
        lista.append(value)
    else:
        print('Valores duplicados não serão adicionados')
    continuar = input('Quer continuar? (S/N)').strip().upper()[0]
    while continuar not in ('S', 'N'):
        continuar = input('Valor inválido, digite ou S ou N: ').strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(lista)