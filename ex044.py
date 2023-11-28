produto = float(input("Digite o preço do produto? "))
pag = int(input("""FORMAS DE PAGAMENTO:

[ 1 ] DINHEIRO/CHEQUE: À VISTA
[ 2 ] CARTÃO: À VISTA
[ 3 ] CARTÃO: 2X
[ 4 ] CARTÃO: 3X OU MAIS

Opção escolhida: """))
if pag == 1:
    print(f"Com 10% de desconto, em dinheiro/cheque, o produto fica custando R${produto * 90 / 100:.2f}.")
elif pag == 2:
    print(f"Com 5% de desconto, à vista no cartão, o produto fica custando R${produto * 95 / 100:.2f}.")
elif pag == 3:
    print(f"O produto fica custando R${produto} ou 2x de R${produto / 2:.2f} sem juros.")
elif pag == 4:
    parc = int(input("Parcelas: "))
    print(f"Com 20% de juros no cartão, o produto fica custando {parc}x R${produto * (120 / 100) / parc:.2f}", end='')
    print(f" ou R${produto * 120 / 100:.2f}.")

if 1 <= pag <= 4:
    print("OBRIGADO PELA PREFERÊNCIA!")
else:
    print("Opção INVÁLIDA! Tente novamente.")
