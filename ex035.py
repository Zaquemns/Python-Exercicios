a = float(input('Digite o comprimento da reta A: '))
b = float(input('Digite o comprimento da reta B: '))
c = float(input('Digite o comprimento da reta C: '))

if a < b + c and b < a + c and c < a + b:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')
