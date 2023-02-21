matriz = [[],[],[]]
for i in range(0, 9):
    n = int(input(f'Valor {i+1}: '))
    if i < 3:
        matriz[0].append(n)
    elif i < 6:
        matriz[1].append(n)
    else:
        matriz[2].append(n)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')