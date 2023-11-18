produto = float(input("Digite o preço do produto? "))
v = 'vista'
p = 'parcelado'
pag = str(input("O pagamento será à vista ou parcelado? Digite somente a inicial: "))

if pag == v:
    print(f"Pagamento selecionado: {v}")
