from datetime import date
atual = date.today().year
ano = 0
sexo = str(input("""Digite seu sexo:
 
    [ M ] MASCULINO     [ F ] FEMININO

Opção escolhida: """)).strip().lower()

if sexo == "f" or sexo == "feminino":
    print("Você está isenta do serviço militar obrigatório!")
elif sexo == "m" or sexo == "masculino":
    print("Todos os brasileiros do sexo masculino deverão se alistar para serviço militar obrigatório!")
    ano = int(input("Digite o ano do seu nascimento: "))
    if atual - ano < 18:
        print(f"Seu alistamento não chegou. Será daqui a {18 - (atual - ano)} ano(s), em {(ano + 18)}.")
    elif atual - ano == 18:
        print(f"Você tem ou completará 18 anos em {atual}. A sua hora chegou.\nALISTE-SE JÁ!")
    else:
        print(f"Seu tempo de alistamento ocorreu há {atual - ano - 18} ano(s) atrás, em {(ano + 18)}.")
else:
    print("OPÇÃO INVÁLIDA! Tente novamente.")
