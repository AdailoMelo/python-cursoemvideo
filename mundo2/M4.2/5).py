#passo 1: Ler o nome e preço dos produtos
#passo 2: Criar um laço de repetição com while perguntando se o usuário tem outro produto para adicionar
#passo 3: mostrar o total gasto na compra
#passo 4: mostrar quantos produtos custam mais de R$1000
#passo 5: mostrar o nome do produto mais barato
#condicional para pegar o produto mais barato = gambiarra

caro = total = 0 
barato = 111111111111111111111111111111111
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    total += preco
    if preco > 1000:
        caro += 1
    if preco < barato:
        nomeb = nome
        barato = preco
    pergunta = input('Você quer adicionar outro produto? (S/N): ').strip().upper()[0]
    if pergunta not in ('S', 'N'):
        while pergunta not in ('S', 'N'):
            pergunta = input('Resposta invalida, digite (S/N)').strip().upper()[0]
    if pergunta == 'N':
        break
print(f'O total a pagar é {total:.2f}, {caro} produtos custam mais de R$1000, o produto mais barato foi {nomeb}')
