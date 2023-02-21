nums = int(input('Número: ')), int(input('Número: ')), int(input('Número: ')), int(input('Número: '))
posicao = nums.index(3)
print(f'Dentre os números digitados tem {nums.count(9)} números 9')
print(f'O primeiro número 3 aparece na posição: {posicao + 1}')
print('Os pares são: ', end='')
for num in nums:
    if num % 2 == 0:
        print(num, end= ' ')
    