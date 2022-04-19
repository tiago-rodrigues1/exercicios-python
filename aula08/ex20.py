from random import shuffle

aluno1 = str(input('- Nome do 1º aluno: '))
aluno2 = str(input('- Nome do 2º aluno: '))
aluno3 = str(input('- Nome do 3º aluno: '))
aluno4 = str(input('- Nome do 4º aluno: '))

alunosLista = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunosLista)

print('\nA ordem de apresentação será:\n{}'.format(alunosLista))
