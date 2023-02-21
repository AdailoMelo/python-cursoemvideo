palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavras in palavra:
    print(f'{palavras}:', end=' ')
    for letras in palavras:
        if letras in 'AEIOU':
            print(letras.lower(), end=' ')
    print()
            