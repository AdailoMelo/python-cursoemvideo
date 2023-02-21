golpartidas = []
jogador = {'nome':input('Nome do jogador: ').title(), 'partidas':int(input('Número de partidas jogadas: '))}
for i in range(0, jogador['partidas']):
    gols = int(input(f' Gols feitos na partida {i+1}: '))
    golpartidas.append(gols)
    if i == 0:
        jogador['total de gols'] = gols
    else:
        jogador['total de gols'] += gols
jogador['gols'] = golpartidas[:]
print(jogador)
print(f'{"-="*30}\n{"== ANALISE ==":^60}')
for k, v in jogador.items():
    if k != 'gols':
        print(f'{k.title()}: {v}')
pergunta = input('Você quer ver quantos gols você fez em cada partida S/N? ').strip().upper()[0]
while pergunta not in 'SN':
    pergunta = input('Responda S/N').strip().upper()[0]
if pergunta == 'S':
    print('-='*30)
    for pos, dados in enumerate(golpartidas):
        print(f'Na {pos+1}° partida {jogador["nome"]} fez {dados} gols')
    print(f'Total de {jogador["total de gols"]} gols')
print('FIM DO PROGRAMA')