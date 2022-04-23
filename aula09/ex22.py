nome = str(input('- Digite seu nome completo: '))

nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
nomeTamanho = len(nome) - nome.count(' ')
primeiroNome = nome.split()[0]
primeiroNomeTamanho = len(primeiroNome)

print('Seu nome em maiúsculas: {}'.format(nomeMaiusculo))
print('Seu nome em minúsculas: {}'.format(nomeMinusculo))
print('Seu nome tem {} letras'.format(nomeTamanho))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiroNome, primeiroNomeTamanho))

