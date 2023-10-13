km = float(input('Digite a distância da viagem em KM: '))
v1 = km * 0.5
v2 = km * 0.45

if km <= 200:
    print(f'A passagem custa R${v1}.')
else:
    print(f'A passagem custa R${v2}.')
