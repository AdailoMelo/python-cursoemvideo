from math import sin, cos, tan, radians
num = int(input('Digite o ângulo: '))
numr = radians(num)
print('O seno de {} é {:.2f}, O cosseno de {} é {:.2f}, e a tangente de {} é {:.2f}'.format(num, sin(numr), num, cos(numr), num, tan(numr)))