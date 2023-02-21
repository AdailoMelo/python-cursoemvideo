pt = int(input('Primeiro termo: '))
razao = int(input('PROGRESSÃO ARITIMÉTICA = '))
decimo = pt + (10-1) * razao
for i in range(pt, decimo + razao, razao):
    print(i)