from datetime import date
ano = date.today().year
nas = int(input('Data de nascimento do(a) Nadador(a): '))
idade = ano - nas
print(f'O ou A atleta tem {idade} ano(s)')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')