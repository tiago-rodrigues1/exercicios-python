diasAlugados = int(input('- Quantidade de dias alugados: '))
kmRodados = int(input('- Quantidade de KM rodados: '))

precoDias = diasAlugados * 60
precoKm = kmRodados * 0.15
precoTotal = precoDias + precoKm

print('O total a pagar é R$ {:.2f}'.format(precoTotal))
