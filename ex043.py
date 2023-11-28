h = float(input("Digite sua altura: "))
w = float(input("Digite seu peso: "))
imc = w / (h ** 2)
print(f"Seu IMC é de {imc:.1f}.", end=' ')
if imc < 18.5:
    print("VOCÊ ESTÁ ABAIXO DO PESO!")
elif imc < 25:
    print("VOCÊ ESTÁ NO PESO IDEAL!")
elif imc < 30:
    print("VOCÊ ESTÁ COM SOBREPESO!")
elif imc < 40:
    print("VOCÊ ESTÁ COM OBESIDADE!")
else:
    print("VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!")
