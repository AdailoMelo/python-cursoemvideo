from datetime import date
ano = date.today().year
nas = int(input('Sua data de nascimento: '))
sex = input('Digite M se você é Homem, ou F se você é Mulher: ').upper().strip()
print(f'Quem nasceu em {nas}, tem ou vai fazer {ano - nas} ano(s) em {ano}')
if sex == 'M':
    if ano - nas < 18:
        print(f'Falta {((ano - nas) - 18) * -1} ano(s) para que você possa se alistar: ')
    elif ano - nas == 18:
        print(f'Você se alista nesse ano')
    else:
        confirm = input('Você ja se alistou? ').strip().title()
        if confirm == 'Sim':
            print('Ótimo')
        else:
            print(f'Seu alistamento está {(ano - nas) - 18} ano(s) atrasado')
else:
    print('No Brasil mulheres não são obrigadas a se alistar no Exercito militar')
    pergunta = input('Caso você queira se alistar mesmo assim digite Quero: ').title().strip()
    if pergunta == 'Quero':
        if ano - nas < 18:
            print(f'Falta {((ano - nas) - 18) * -1} ano(s) para que você possa se alistar: ')
        elif ano - nas == 18:
            print(f'Você pode se alistar nesse ano')
        else:
            print(f'Você pode se alistar ja faz(em) {(ano - nas) - 18} ano(s)')
    else:
        print('Ok')