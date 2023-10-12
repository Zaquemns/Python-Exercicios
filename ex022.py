nome_completo = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é {nome_completo.upper()}.')
print(f'Seu nome em minúsculas é {nome_completo.lower()}.')
nome_completo2 = str((nome_completo.replace(' ', '')))
print(f'Seu nome tem {len(nome_completo2)} letras no total.')
lista_nome = [nome_completo.split()]
primeiro_nome = lista_nome[0]
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras.')
