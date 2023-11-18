from random import choice

pedra = str("pedra")
papel = str("papel")
tesoura = str("tesoura")
str(print("JO KEN PO..."))
res = str(input("Escolha: pedra, papel ou tesoura? "))
jkp = ["pedra", "papel", "tesoura"]
res0 = choice(jkp)
print(f"Eu escolho: {res0.upper()}")
print(f"Você escolhe: {res.upper()}")
print(f"{res0.upper()} VS {res.upper()}")

if res == res0:
    print("DEU EMPATE!")
elif res != res0:
    if res == papel and res0 == pedra or res == pedra and res0 == tesoura or res == tesoura and res0 == papel:
        print(f"{res.upper()} derrota {res0.upper()}. VOCÊ VENCEU!")
    else:
        print(f"{res0.upper()} derrota {res.upper()}. EU VENCI!")
