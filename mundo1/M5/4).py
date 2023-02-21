d = float(input('Qual é a distância do lugar para onde você quer ir: '))
if d <= 200:
    print(f'O preço da passagem é: R${d * 0.50:.2f}')
else:
    print(f'O preço da passagem é: R${d * 0.45:.2f}')