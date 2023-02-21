pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input('Digite seu nome: '))
    dados.append(int(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? S/N: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Quer continuar? S/N: ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
for cadastro in pessoas:
    if cadastro[1] == maior:
        print(f'{cadastro[0]} está entre as pessoas mais pesadas')
for cadastro in pessoas:
    if cadastro[1] == menor:
        print(f'{cadastro[0]} está entre as pessoas menos pesadas')