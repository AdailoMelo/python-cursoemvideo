aluno = {}
aluno['nome'] = (input('Nome: ')).title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
    if aluno['media'] == 10:
        print('Nota máxima, parabéns')
elif aluno['media'] < 7 and aluno['media'] > 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'A situação de {aluno["nome"]} é: {aluno["situação"]}')