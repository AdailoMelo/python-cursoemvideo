#tipo primitivo, Só tem espaços? É um número? É alfabético? É alfanumérico? Está em maiusculas? Está em minúsculas? Está capitalizada 

algo = input("digite algo: ")
print(f'O tipo primitivo de {algo} é {type(algo)}')
print(f'{algo} só tem espaços? {algo.isspace()}')
print(f'{algo} é um número? {algo.isnumeric()}')
print(f'{algo} é alfabético? {algo.isalpha()}')
print(f'{algo} é alfanumérico? {algo.isalnum()}')
print(f'{algo} esta em maiusculas? {algo.isupper()}')
print(f'{algo} esta em minusculas? {algo.islower()}')
print(f'{algo} está captalizada? O que é capitalizada?') 
print('capitalizada significa ter caracteres maiúsculos e minúsculos dentro da variavel')
print(f'{algo} está captalizada? {algo.istitle()}')