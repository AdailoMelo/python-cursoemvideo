jogadores = []
golpartidas = []
goljogadores = []
while True:
    jogador = {'nome':input('Digite o nome do jogador: '), 'partidas':int(input(f'Quantas partidas jogou? '))}
    for gols in range(0, jogador['partidas']):
        if gols == 0:
            jogador['totalgols'] = int(input(f'Quantos gols foram feitos na partida {gols+1}: '))
            golpartidas.append(jogador['totalgols'])
        else:
            gol = int(input(f'Quantos gols foram feitos na partida {gols+1}: '))
            golpartidas.append(gol)
            jogador['totalgols'] += gol
    goljogadores.append(golpartidas[:])
    golpartidas.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    pergunta = input('Quer continuar? ').strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = input('Digite S ou N').strip().upper()[0]
    if pergunta == 'N':
        break
print('-='*30)
for pos, dados in enumerate(jogadores):
    if dados['partidas'] == 0:
        print(f"[{pos}] {dados['nome']} {'-'*(30-len(dados['nome']))} 0")
    else:
        print(f"[{pos}] {dados['nome']} {'-'*(30-len(dados['nome']))} {dados['totalgols']}")
print('-='*30)
while True:
    codigo = int(input('Digite o código do jogador que você quer ver o desenpenho individual do jogador (999 para finalizar): '))
    if codigo == 999:
        break
    for pos, gols in enumerate(goljogadores[codigo]):
        print(f'{jogadores[codigo]["nome"]} fez {goljogadores[codigo][pos]} gols na partida {pos+1}')
print('VOLTE SEMPRE!')