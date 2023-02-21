#passo 1: fazer com que o computador escolha um número (de 0 a 10 que é quantos dedos um humano tem na mão) FEITO
#passo 2: pegar a entrada do usuário e somar com a do computador FEITO
#passo 3: pegar a escolha do usuário (impar ou par) FEITO
#passo 4: criar o laço de repetição

from random import randint
bot = randint(0, 10)
num = int(input('Escolha seu número (de 0 a 10): '))
ganhou = 0
while True:
    escolha = input('Impar ou Par? ').strip().upper()[0]
    resultado = bot + num
    if escolha in ('I', 'P'):
        if num % 2 == 0 and escolha == 'P':
            print(f'Ganhou, você colocou {num} e o bot colocou {bot} o resultado final é {resultado}')
            ganhou += 1
            bot = randint(0, 10)
            num = int(input('Escolha seu número (de 0 a 10): '))
        elif num % 2 != 0 and escolha == 'I':
            print(f'Ganhou, você colocou {num} e o bot colocou {bot} o resultado final é {resultado}') 
            ganhou += 1
            bot = randint(0, 10)
            num = int(input('Escolha seu número (de 0 a 10): '))
        elif num % 2 != 0 and escolha == 'P':
            print(f'Perdeu, você colocou {num} e o bot colocou {bot} o resultado final é {resultado}')
            break
        elif num % 2 == 0 and escolha == 'I':
            print(f'Perdeu, você colocou {num} e o bot colocou {bot} o resultado final é {resultado}')
            break

print(f'Fim do programa, você ganhou {ganhou} vezes')