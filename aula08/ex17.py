import math

catOposto = float(input('- Comprimento do cateto oposto: '))
catAdjacente = float(input('- Comprimento do cateto adjacente: '))

hipotenusa = math.hypot(catOposto, catAdjacente)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
