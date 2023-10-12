n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'A unidade é {u}.')
print(f'A dezena é {d}.')
print(f'A centena é {c}.')
print(f'O milhar é {m}.')
