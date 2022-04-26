VELOCIDADE_LIMITE = 80
velocidadeMotorista = int(input('- Qual é a velocidade atual do carro: '))

if velocidadeMotorista > VELOCIDADE_LIMITE:
    valorMulta = (velocidadeMotorista - VELOCIDADE_LIMITE) * 7
    print('Você está acima do limite de velocidade. Valor da multa: R${:.2f}'.format(valorMulta))

print('Tenha um bom dia! Dirija com segurança!')

