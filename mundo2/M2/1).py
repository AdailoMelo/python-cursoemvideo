casa = float(input('Quanto custa a casa? '))
salario = float(input('Quanto você ganha? '))
anos = float(input('A casa vai ser parcelada em quantos anos? '))
parcela = casa / (anos*12)
if salario * 0.3 <= parcela:
    print('Emprestimo não pode ser feio')
else:
    print('Emprestimo pode ser feito')