from random import randint

jkp = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
str(print("""Escolha: 

[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
"""))

jog = int(input("Sua escolha: "))
print(f"Eu escolho {jkp[cpu]}.")
print(f"Você escolhe {jkp[jog]}.")
print(f"{jkp[cpu]} VS {jkp[jog]}.")

if jog != cpu:
    if jog == 0 and cpu == 2 or jog == 1 and cpu == 0 or jog == 2 and cpu == 1:
        print(f"{jkp[jog]} derrota {jkp[cpu]}. VOCÊ VENCEU!")
    else:
        print(f"{jkp[cpu]} derrota {jkp[jog]}. EU VENCI!")
else:
    print("DEU EMPATE!")
