p18 = h = m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()[0]
    if sexo not in ('M', 'F'):
        while sexo not in ('M', 'F'):
            sexo = input('Sexo (M/F): ').strip().upper()[0]
    if sexo == 'M':
        h += 1
    else: 
        if idade < 20:
            m20 += 1
    if idade >= 18:
        p18 += 1
    
    pergunta = input('Cadastro feito, quer parar por aqui? (S/N) ').strip().upper()[0]
    if pergunta not in ('S', 'N'):
        while pergunta not in ('S', 'N'):
            pergunta = input('Resposta invalida, digite (S/N) ').strip().upper()[0]
    if pergunta == 'S':
        break

print(f'Foram cadastrados {p18} pessoas maiores de idade, {h} homens, e {m20} mulheres com menos de 20 anos')