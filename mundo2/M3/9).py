from datetime import date
ano = date.today().year
cont = 0
for i in range(7):
    nascimento = int(input('Ano de nascimento: '))
    if ano - nascimento >= 18:
        cont += 1
print(f'{cont} Pessoas já são maiores de idade')
print(f'{7-cont} Pessoas ainda não são maiores de idade')