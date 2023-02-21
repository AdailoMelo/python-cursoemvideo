def ficha(n='<desconhecido>', g=0):
    
    print(f'O jogador {n} marcou {g} gols na temporada')
    
nome = input('Nome: ').strip()
gols = input('Gols: ').strip()
if gols.isnumeric() == True:
    gols = int(gols)
else:
    gols = 0
if nome == '':
    nome = '<desconhecido>'
ficha(nome, gols)