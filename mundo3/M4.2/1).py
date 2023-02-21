def voto(nascimento):
    """A função voto pega sua data de nascimento e diz se você pode, não pode, ou é obrigado a votar."""
    from datetime import date
    if nascimento > date.today().year:
        print('Você não nasceu ainda')
    else:
        idade = date.today().year - nascimento
        if idade < 16:
            print(f'Com {idade} anos. Não vota!')
        elif idade >= 18 and idade <= 65:
            print(f'Com {idade} anos. Voto obrigatório')
        else:
            print(f'Com {idade} anos. Voto opcional!')


#main program
data = int(input('Digite o ano em que você nasceu: '))
voto(data)