n = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão: 
[ 1 ] BINÁRIO
[ 2 ] HEXADECIMAL
[ 3 ] OCTAL""")
op = int(input("Opção selecionada: "))
if op == 1:
    print(f"O número {n} convertido em BINÁRIO é {bin(n)[2:]}.")
elif op == 2:
    print(f"O número {n} convertido em HEXADECIMAL é {hex(n)[2:]}.")
elif op == 3:
    print(f"O número {n} convertido em OCTAL é {oct(n)[2:]}.")
else:
    print("OPÇÃO INVÁLIDA!\nTente novamente.")
