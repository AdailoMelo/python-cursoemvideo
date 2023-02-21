def area(largura, comprimento):
    print(f'A área de um terreno de {largura}x{comprimento} é de {largura*comprimento:.2f}m²')

L = float(input('Largura: '))
C = float(input('Comprimento: '))
area(L, C)