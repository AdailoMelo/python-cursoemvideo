largura = float(input('Largura da parede '))
altura = float(input('Altura da parede: '))
area = largura * altura
litros = area / 2
print(f'Para pintar uma parede de {altura:.2f} de altura e {largura:.2f} de largura, é necessário {litros:.2f} litros de tinta')
