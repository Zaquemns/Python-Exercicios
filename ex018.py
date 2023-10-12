import math
x = float(input('Digite o valor do ângulo em graus: '))
xrad = math.radians(x)
sin = math.sin(xrad)
cos = math.cos(xrad)
tan = math.tan(xrad)
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(x, sin, cos, tan))


