nomeCompleto = str(input('- Informe seu nome completo: ')).strip().lower()

nomes = nomeCompleto.split()

print('Seu nome tem Silva ? {}'.format('silva' in nomes))
