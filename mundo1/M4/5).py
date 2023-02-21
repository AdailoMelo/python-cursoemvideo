from random import shuffle
a1 = input('Aluno(a): ')
a2 = input('Aluno(a): ')
a3 = input('Aluno(a): ')
a4 = input('Aluno(a): ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'Ordem de apresentação: {alunos}')
