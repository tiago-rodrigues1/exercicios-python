frase = str(input('- Digite uma frase: ')).strip().lower()

chave = "a"

quantidadeOcorrencias = frase.count(chave)
primeiraOcorrencia = frase.find(chave)
ultimaOcorrencia = frase.rfind(chave)

print('A letra {} aparece {} vezes na frase'.format(chave, quantidadeOcorrencias))
print('A primeira letra {} aparece na posição {}'.format(chave, (primeiraOcorrencia + 1)))
print('A última letra {} aparece na posição {}'.format(chave, (ultimaOcorrencia + 1)))
