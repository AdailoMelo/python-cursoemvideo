def fatorial(num, show=False):
    """-> Calcula o Fatorial de um número.\n:para n: O número a ser calculado.\n:Para show: (opcional) Mostrar ou não a conta."""
    fator = cont = 0
    fnum = num
    for fat in range(num):
        if show == True:
            if num >= 2:
                print(f'{num} x', end=' ', flush=True)
            else:
                print(f'{num} = {fator}')
        if fat == 0:
            fator = num
        else:
            fator *= num
        num -= 1
    if show == False:
        return fator

help(fatorial)
print(fatorial(4))
print(fatorial(3))
fatorial(int(input('Escolha o valor que você deseja saber o fatorial: ')), True)