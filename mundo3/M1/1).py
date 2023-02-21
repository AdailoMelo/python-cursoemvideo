num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    mostrar = int(input('Digite um número entre 0 a 20: '))
    if mostrar > 20 or mostrar < 0:
        mostrar = int(input('Tente denovo. Digite um número entre 0 a 20: '))
    else:
        print(num[mostrar])
    pergunta = input('Quer continuar (S/N)? ').strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = input('Quer continuar (S/N)? ').strip().upper()[0]
    if pergunta == "N":
        break