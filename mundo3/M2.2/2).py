valores = [[], []]
for i in range(7):
    n = int(input(f'Digite o {i+1}o valor: '))
    if n % 2 == 0:
        valores[1].append(n)
    else:
        valores[0].append(n)
valores[0].sort()
valores[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {valores[1]}\nOs valores Ímpares digitados foram {valores[0]}')