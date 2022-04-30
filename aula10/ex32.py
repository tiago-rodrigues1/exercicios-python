ano = int(input('- Informe um ano: '))

isBissexto = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))

if isBissexto:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
