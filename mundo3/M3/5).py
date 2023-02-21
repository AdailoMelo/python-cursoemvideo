pessoas = []
while True:
    dados = {'nome':input('Digite seu nome: '), 'sexo':input('Qual é o seu sexo? M/F: ').strip().upper()[0], 'idade':int(input('Quantos anos você tem?: '))}
    while dados['sexo'] not in 'MF':
        dados['sexo'] = input('Infelizmente para deixar as coisas mais simples, só podemos aceitar o sexo como Masculino ou Feminino, digite M ou F: ').strip().upper()[0]
    pessoas.append(dados.copy())
    dados.clear()
    pergunta = input('Quer continuar? S/N: ').strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = input('Digite S para sim ou N para não: ').strip().upper()[0]
    if pergunta == 'N':
        break
print(f'{"-="*30}\n{len(pessoas)} pessoas foram cadastradas')
idade_media = 0
for media in pessoas:
    idade_media += media['idade']
print(f'A média de idade das pessoas cadastradas é: {idade_media // len(pessoas)}')
print(f'As mulheres cadastradas foram:')
for mulheres in pessoas:
    if mulheres['sexo'] == 'F':
        print(mulheres['nome'])
print('Pessoas com idade acima da média do grupo:')
for media in pessoas:
    if idade_media // len(pessoas) < media['idade']:
        print(media['nome'])   