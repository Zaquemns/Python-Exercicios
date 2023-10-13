a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a > b and c > b:
    menor = b
if a > c and b > c:
    menor = c
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
