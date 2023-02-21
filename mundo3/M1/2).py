brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético Paranaense', 'Atlético mineiro', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goias', 'Red bull bragantino', 'Coritiba', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
#os 5 primeiros
print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
#os 4 ultimos
print(f'Os 4 ultimos colocados são: {brasileirao[15:]}')
#Ordem alfabética
print(f'Os times em ordem alfabética ficam assim: {sorted(brasileirao)}')
#Onde está o corinthians
print('O corinthians está na posição:', brasileirao.index('Corinthians') + 1)