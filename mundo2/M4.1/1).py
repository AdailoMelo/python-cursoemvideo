sexo = input('Digite M pra homem ou F para mulher: ').strip().upper()[0]
while sexo not in ('MF'):
    sexo = input('Opção invalida, tente novamente: ').strip().upper()
print('Você é um Homem' if sexo == 'M' else 'Você é uma Mulher')