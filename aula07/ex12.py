precoProduto = float(input('- Preço do produto: '))

desconto = precoProduto * 0.05

novoPreco = precoProduto - desconto

print('\nR${:.2f} com 5% de desconto é: R${:.2f}'.format(precoProduto, novoPreco))
