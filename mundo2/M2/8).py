p = float(input('Quanto você pesa? '))
h = float(input('Qual é a sua altura? '))
imc = p / (h**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')