matriz = [[],[],[]]
maior = soma = 0
for i in range(0, 9):
    n = int(input(f'Valor {i+1}: '))
    if i < 3:
        matriz[0].append(n)
        if n % 2 ==0:
            soma += n
    elif i < 6:
        matriz[1].append(n)
        if n % 2 ==0:
            soma += n
    else:
        matriz[2].append(n)
        if n % 2 ==0:
            soma += n
print('-='*30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print(f'A soma dos valores pares é:\n{soma}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é:\n{soma}')
for valor in matriz[1]:
    if valor > maior:
        maior = valor
print(f'O maior valor da segunda linha é:\n{maior}')