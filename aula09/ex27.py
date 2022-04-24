nomeCompleto = str(input('- Digite seu nome completo: ')).strip()

nomes = nomeCompleto.split()

primeiroNome = nomes[0]
ultimoNome = nomes[len(nomes) - 1]

print('Seu primeiro nome é {}'.format(primeiroNome))
print('Seu último nome é {}'.format(ultimoNome))
