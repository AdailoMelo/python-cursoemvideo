ano = int(input('Qual ano você quer saber se é bisexto?: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('É bisexto')
else:
    print('Não é bisexto')