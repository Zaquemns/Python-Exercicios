s = float(input('Digite o valor do seu salário: '))
a1 = s + (s * 10 / 100)
a2 = s + (s * 15 / 100)

if s <= 1250:
    print(f' Seu novo salário é R${a2:.2f}.')
else:
    print(f'Seu novo salário é R${a1:.2f}.')
