from UtilidadesCeV.moeda import resumo
n = int(input('Digite o valor que você quer receber as informações: R$'))
pergunta = input('Quer calcular a taxa? S/N: ').strip().upper()[0]
if pergunta == 'S':
    ta = int(input('Taxa de aumento: '))
    tr = int(input('Taxa de redução: '))
    resumo(n, ta, tr)
else:
    resumo(n)