#NEED TO REMAKE
num = []
pmaior = []
pmenor = []
maior = menor = 0

for i in range(0, 5):     #Armazenando dados em uma lista e descobrindo qual é o maior e o menor
    num.append(int(input(f'Digite um número para a posição {i}: ')))
    if i == 0:
        maior = menor = num[i]
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]
for posicao in range(len(num)):      #Guardando as posições em listas
    if maior == num[posicao]:
        pmaior.append(posicao)
    elif menor == num[posicao]:
        pmenor.append(posicao)
print(f'O maior número foi {maior} nas posições {pmaior}')
print(f'O menor número foi {menor} nas posições {pmenor}')