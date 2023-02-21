from time import sleep
def contador(início, fim, passo):
    if passo > 0:
        print(f'Contagem de {início} a {fim} de {passo} em {passo}')
    else:
        print(f'Contagem de {início} a {fim} de {passo*-1} em {passo*-1}')
    if passo > 0:
        for c in range(início, fim+1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('Fim')
    elif passo < 0:
        for c in range(início, fim-1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('Fim')
    else:
        for c in range(início, fim+1, 1):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('Fim')
    print('-='*30)

print('-='*30)
contador(1, 10, 1)
contador(10, 0, -2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo (Usar número negativo caso queira fazer uma contagem regressiva.): '))
print('-='*30)
contador(i, f, p)