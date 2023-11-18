a = float(input("Digite o comprimento da reta a: "))
b = float(input("Digite o comprimento da reta b: "))
c = float(input("Digite o comprimento da reta c: "))

if a + b > c and a + c > b and a < b + c:
    print("O triângulo existe!")
    if a == b == c:
        print("O triângulo é EQUILÁTERO!")
    elif a == b or a == c or b == c:
        print("O triângulo é ISÓSCELES!")
    elif a != b != c:
        print("O triângulo é ESCALENO!")
else:
    print("O triângulo não existe!")
