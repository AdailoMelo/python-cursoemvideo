lista = []
dados = []
media = 0
while True:
    dados.append(input('Nome do aluno: '))
    dados.append(float(input('Primeira nota: ')))
    dados.append(float(input('Segunda nota: ')))    
    lista.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? S/N: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Digite S ou N: ').strip().upper()[0]
    if continuar == 'N':
        break

print('-='*30)
print('MÉDIA DOS ALUNOS: ')
for aluno in lista[:]:
    media = (aluno[1] + aluno[2]) / 2
    print(f'{aluno[0]}', end='.'*(30-len(aluno[0])))
    print(f'{media:.2f}')
print(aluno)
while True:
    continuar = input('Você quer ver as notas de algum aluno individual? Digite (S/N): ').strip().upper()[0]
    if continuar == 'S':
        notas_individuais = (input('Digite o nome do aluno que você quer ver as notas: '))
        for alunos in lista[:]:
            if alunos[0] == notas_individuais:
                print(f'As notas desse aluno foram: {alunos[1]} e {alunos[2]}')
    if continuar == 'N':
        break
print('FIM DO PROGRAMA, VOLTE SEMPRE')