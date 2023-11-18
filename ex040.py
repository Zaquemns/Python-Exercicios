n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

if m < 5:
    print(f"Sua média foi de {m}.\nVOCÊ FOI REPROVADO!")
elif m < 7:
    print(f"Sua média foi de {m}.\nVOCÊ ESTÁ DE RECUPERAÇÃO!")
elif m <= 10:
    print(f"Sua média foi de {m}.\nVOCÊ FOI APROVADO!")