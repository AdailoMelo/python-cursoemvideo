maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input('Quanto você pesa?: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    if maior_peso < peso: 
        maior_peso = peso
    if menor_peso > peso:
        menor_peso = peso
print(f'O maior peso foi {maior_peso}Kg e o menor peso foi {menor_peso}Kg')