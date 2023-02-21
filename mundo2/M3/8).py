frase = input('Digite algo: ')
palavras = frase.split()
junto = ''.join(palavras)
if junto == junto[::-1]:
    print('Palíndromo')
else:
    print('Não é palíndromo')