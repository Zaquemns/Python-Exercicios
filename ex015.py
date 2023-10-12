d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos com o carro? '))
p = (d * 60) + (km * 0.15)
print('O valor total do aluguel foi de R${:.2f}.'.format(p))
