from random import choice
from time import sleep
jokenpo = ['Pedra', 'Papel', 'Tesoura']
jokenpo = choice(jokenpo).upper().strip()
escolha = input('Pedra, Papel ou Tesora?: ').upper().strip()
if escolha == 'PEDRA' and jokenpo == 'PEDRA' or escolha == 'PAPEL' and jokenpo == 'PAPEL' or escolha == 'TESOURA' and jokenpo == 'TESOURA':
    sleep(1.5)
    print('Empate!')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'PEDRA' and jokenpo == 'TESOURA':
    sleep(1.5)
    print('Ganhou')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'PAPEL' and jokenpo == 'PEDRA':
    sleep(1.5)
    print('Ganhou')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'TESOURA' and jokenpo == 'PAPEL':
    sleep(1.5)
    print('Ganhou')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'PEDRA' and jokenpo == 'PAPEL':
    sleep(1.5)
    print('Perdeu')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'PAPEL' and jokenpo == 'TESOURA':
    sleep(1.5)
    print('Perdeu')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
elif escolha == 'TESOURA' and jokenpo == 'PEDRA':
    sleep(1.5)
    print('perdeu')
    print(f'Eu escolhi: {escolha.title()} e o computador escolheu: {jokenpo.title()}')
else:
    print('Algo está errado')
    print(f'Eu escolhi: {escolha.upper()} e o computador escolheu: {jokenpo.title()}')