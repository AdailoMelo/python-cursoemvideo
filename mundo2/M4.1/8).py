soma = cont_d = 0 
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont_d += 1
    n = int(input('(digite 999 pra parar), Digite um número: '))
print(f'A soma de todos os elementos digitados foi: {soma} e foram digitados {cont_d} elementos')