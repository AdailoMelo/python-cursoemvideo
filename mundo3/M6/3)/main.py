from lib.Interface import *
from lib.Arquivo import *

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArquivo(arq)

L = ['Mostrar pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do sistema']
menu(L)
