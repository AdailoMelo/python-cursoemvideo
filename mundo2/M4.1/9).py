cont = 1
soma = nota = float(input('Nota: '))
confirma = input('Quer colocar mais uma nota? (S/N): ').strip().upper()
while confirma == 'S':
    nota = float(input('Próxima nota: '))
    soma += nota
    cont += 1
    confirma = input('Quer colocar mais uma nota? (S/N): ').strip().upper()[0]
print(f'Você digitou {cont} notas, A média das notas é: {soma/(cont):.2f}')
