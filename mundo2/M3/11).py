cont = 0
contf = 0
h_mv = 0
nome = 'None'
for i in range(1, 5):
    name = input(f'{i}° Nome: ').title().strip()
    age = int(input('Idade: '))
    sexo = input('Sexo(M/F): ').upper().strip()
    cont += age
    if sexo == 'M' and age > h_mv:
        h_mv = age
        nome = name
    elif sexo == 'F':
        if age < 20:
            contf += 1
media = cont / 4
print(f'Idade média = {media:.0f}')
print(f'Homem mais velho tem {h_mv} anos e seu nome é {nome}')
print(f'{contf} Mulheres tem menos de 20 anos')