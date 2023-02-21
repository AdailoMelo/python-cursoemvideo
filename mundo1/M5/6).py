n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2:
    if n1 > n3:
        print(f'{n1} é o maior número dos 3')
        if n2 > n3:
            print(f'{n3} é o menor número dos 3')
        else:
            print(f'{n2} é o menor número dos 3')
    else:
        print(f'{n3} é o maior número dos 3')
        print(f'{n2} é o menor número dos 3')
else:
    if n2 > n3:
        print(f'{n2} é o maior dos 3')
        if n1 > n3:
            print(f'{n3} é o menor dos 3')
        else:
            print(f'{n1} é o menor dos 3')
    else:
        print(f'{n3} é o maior dos 3')
        print(f'{n1} é o menor dos 3')