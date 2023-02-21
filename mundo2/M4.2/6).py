#Cédulas, 50, 20, 10 e 1
#passo 1: O usuario indica quanto ele quer sacar
#passo 2: Usar um sistema de divisão inteira para indicar quantas cédulas de cada serão sacadas
C50 = C20 = C10 = C1 = soma = 0
valor_inicial = valor = int(input('Sacar R$')) 
C50 = valor // 50
valor %= 50
C20 = valor // 20
valor %= 20
C10 = valor // 10
valor %= 10
C1 = valor // 1
print(f'{C50} Cédulas de 50, {C20} cédulas de 20, {C10} cédulas de 10 e {C1} cédulas de 1')

#Tentar fazer com estrutura de repetição quando for revisar