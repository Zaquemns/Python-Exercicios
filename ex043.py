h = float(input("Digite sua altura: "))
w = float(input("Digite seu peso: "))
imc = w / (h * h)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f}.\nVOCÊ ESTÁ ABAIXO DO PESO!")
elif imc < 25:
    print(f"Seu IMC é de {imc:.2f}.\nVOCÊ ESTÁ NO PESO IDEAL!")
elif imc < 30:
    print(f"Seu IMC é de {imc:.2f}.\nVOCÊ ESTÁ COM SOBREPESO!")
elif imc < 40:
    print(f"Seu IMC é de {imc:.2f}.\nVOCÊ ESTÁ COM OBESIDADE!")
elif imc > 40:
    print(f"Seu IMC é de {imc:.2f}.\nVOCÊ ESTÁ COM OBESIDADE MÓRBIDA!")
