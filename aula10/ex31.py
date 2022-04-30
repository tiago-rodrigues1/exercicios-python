distancia = float(input('- Distância da sua viagem: '))

precoPorKm = 0

if distancia <= 200:
    precoPorKm = 0.5
else:
    precoPorKm = 0.45

precoPassagem = precoPorKm * distancia

print('O preço da sua passagem ficou R${:.2f}'.format(precoPassagem))
