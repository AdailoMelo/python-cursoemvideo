lista = []
while True:
    valor = int(input('Valor: '))
    lista.append(valor)
    continuar = input('Quer continuar?: ').strip().upper()[0]
    while continuar not in ('S', 'N'):
        continuar = input('Não entendi! Digite Sim ou Não: ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados: {len(lista)} números nessa lista!')
lista.sort(reverse=True)
print(f'Lista em forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não está na lista')
