from datetime import date
trabalhador = {'nome':input('Digite seu nome: '), 'idade':date.today().year - int(input('Data de nascimento: ')), 'cpts':int(input('Carteira de trabalho (0 = não tem): '))}
if trabalhador['cpts'] == 0:
    print('-='*30)
    for k, mostrar in trabalhador.items():
        print(f'{k.title()} tem o valor {mostrar}')
else:
    trabalhador['contrato'] = int(input('Data em que você foi contratado: '))
    trabalhador['salario'] = float(input('Quanto você recebe: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (35 + trabalhador['contrato']) - date.today().year
    print('-='*30)
    for k, mostrar in trabalhador.items():
        print(f'{k.title()} tem o valor {mostrar}')