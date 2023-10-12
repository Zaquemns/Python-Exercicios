ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print(f'{ano} é ano bissexto.')
else:
    print(f'{ano} não é ano bissexto.')
