soma = digitados = 0

while True:
    num = int(input('Digite números (Digite 999 caso queira parar): '))
    if num == 999:
        break
    soma += num
    digitados += 1
print(f'Foram digitados {digitados} números e a soma de todos eles é {soma}')