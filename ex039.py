from datetime import date
ano = int(input("Digite o ano do seu nascimento: "))
atual = date.today().year

if atual - ano < 18:
    print(f"Sua hora de se alistar ainda não chegou. Será daqui a {18 - (atual - ano)} ano(s).")
elif atual - ano == 18:
    print("A sua hora chegou. ALISTE-SE JÁ!")
elif atual - ano > 18:
    print(f"Seu tempo de alistamento ocorreu há {atual - ano - 18} ano(s) atrás.")
