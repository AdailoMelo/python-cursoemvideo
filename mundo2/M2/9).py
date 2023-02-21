p_i = float(input('Valor do produto, sem juros: '))
pagar = int(input('''Você tem 4 opções:
1 - À vista (Dinheiro/Cheque): desconto de 10%
2 - À vista no cartão: desconto de 5%
3 - Em até 2x no cartão: Valor sem juros
4 - 3x ou mais: Juros de 20%
Qual você escolhe?: '''))
if pagar == 1:
    print(f'Preço a pagar: {p_i * 0.9}')
elif pagar == 2:
    print(f'Preço a pagar: {p_i * 0.95}')
elif pagar == 3:
    print(f'2x de {p_i / 2}')
elif pagar == 4:
    parcela = int(input('Você quer dividir em quantas vezes?'))
    print(f'O valor com os juros passou a ser {p_i * 1.2} parcelado em {parcela}x de {(p_i * 1.2) / parcela}')
else:
    print('Algum engano na hora de escolher a opção? Sem problemas, reinicie o programa e tente novamente.')