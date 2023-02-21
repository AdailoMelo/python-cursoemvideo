salario = float(input('Salário: '))
if salario > 1250:
    print(f'Salario reajustado para: {salario * 1.10:.2f}')
else:
    print(f'Salário reajustado para: {salario * 1.15:.2f}')