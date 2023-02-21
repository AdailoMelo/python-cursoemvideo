def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
from lib.Interface import leiaInt
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            tam = 35-len(dado[0])
            print(f'{dado[0]:<30}', end='')
            print(f'{dado[1]:>5} Anos')
    finally:
        a.close()
def Cadastrar(nome):
    try:
        a = open(nome, 'at')
        n = input('NOME: ')
        i = input('IDADE: ')
        a.write(f'{n};{i}\n')
    except:
        print(f'Houve um erro no cadastro')
    else:
        a.close