import random
a = input('Aluno: ')
b = input('Aluno: ')
c = input('Aluno: ')
d = input('Aluno: ')
alunos = [a, b, c, d]
print(f'O aluno escolhido é {random.choice(alunos)}')