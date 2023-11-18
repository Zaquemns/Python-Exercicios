casa = float(input("Qual o valor da casa? "))
s = float(input("Qual o seu salário? "))
anos = float(input("Em quantos anos você vai pagar o empréstimo? "))
pm = ((casa / anos) / 12)
if pm > s * 30 / 100:
    print(f"O EMPRÉSTIMO FOI NEGADO!\nMotivo: a prestação mensal excede 30% do salário.")
elif pm <= s * 30 / 100:
    print(f"O EMPRÉSTIMO FOI APROVADO!\nAs parcelas mensais serão de {pm:.2f} reais.")
