#JEITO FACIL, VOU FAZER COM WHILE MAS LEMBRAR QUE PODE SER FEITO ASSIM TAMBÉM
#from math import factorial
#n = int(input('De qual número você quer descobrir o fatorial? '))
#print(factorial(n))


ni = n = fatorial = int(input('De qual número você quer descobrir o fatorial? '))
while n >= 2:
    n -= 1
    fatorial *= n
print(f'O fatorial de {ni} é: {fatorial}')