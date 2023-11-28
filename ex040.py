n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

if m < 5:
    print(f"Sua média foi de {m:.1f}.\nVOCÊ FOI REPROVADO!")
elif 5 >= m < 7:
    print(f"Sua média foi de {m:.1f}.\nVOCÊ ESTÁ DE RECUPERAÇÃO!")
else:
    print(f"Sua média foi de {m:.1f}.\nVOCÊ FOI APROVADO!")
