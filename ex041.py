from datetime import date
ano = int(input("Digite o seu ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"Idade: {idade}")
if idade <= 9:
    print("A categoria do atleta é MIRIM!")
elif idade <= 14:
    print("A categoria do atleta é INFANTIL!")
elif idade <= 19:
    print("A categoria do atleta é JÚNIOR!")
elif idade <= 25:
    print("A categoria do atleta é SÊNIOR!")
else:
    print("A categoria do atleta é MASTER!")
