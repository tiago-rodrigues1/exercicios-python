larguraParede = float(input('- Largura da parede: '))
alturaParede = float(input('- Altura da parede: '))

area = larguraParede * alturaParede

quantidadeTinta = area / 2

print('\nSerão necessários {} litros de tinta'.format(quantidadeTinta))
