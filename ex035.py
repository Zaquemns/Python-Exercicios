a = float(input('Digite o comprimento de uma reta A: '))
b = float(input('Digite o comprimento de uma reta B: '))
c = float(input('Digite o comprimento de uma reta C: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
