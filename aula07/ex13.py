salario = float(input('- Salário do funcionário: '))

aumento = salario * 0.15

novoSalario = salario + aumento

print('\nR${:.2f} com 15% de aumento é: R${:.2f}'.format(salario, novoSalario))
