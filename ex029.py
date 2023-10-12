v = int(input('Digite a velocidade do carro: '))
limite = 80
multa = (v - limite) * 7

if v > 80:
    print('Alerta, você foi multado!')
    print(f'O valor da multa foi de R${multa}.')
else:
    print('Você não foi multado!')