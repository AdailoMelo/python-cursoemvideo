from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
ESCOLHA O QUE QUER FAZER: '''))
while escolha != 5:
    if escolha == 1:
        print(f'A soma é igual a: {n1 + n2}')
    elif escolha == 2:
        print(f'A multiplicação é igual a: {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é o maior')
        elif n2 > n1:
            print(f'{n2} é o maior')
        else:
            print('Os dois números são iguais')
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    sleep(2)
    escolha = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
ESCOLHA O QUE QUER FAZER: '''))
print('Tenha um bom dia')