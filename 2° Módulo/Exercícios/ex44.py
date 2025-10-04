#calcule o valor a ser pago considerando seu preço normal e condição de pagamento
# a vista dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# ate 2x no cartao: preco normal
#3x ou mais no cartao: 20% de juros

precoProduto = float(input('Informe o preco do produto: '))
formaPagamento = str(input('Qual a forma de pagamento: '))

if formaPagamento == 'Dinheiro' or formaPagamento == 'Cheque':
    novoPreco = precoProduto - (precoProduto * 0.10)
    print('Você recebeu 10% de desconto, seu novo preço sera de {} '.format(novoPreco))
elif formaPagamento == 'Cartão':
    novoPreco = precoProduto - (precoProduto * 0.05)
    print('Você recebeu 5% de desconto, seu novo preço sera de {}'.format(novoPreco))
elif formaPagamento == '2x no cartão':
    print('Seu preço sera de {}'.format(precoProduto))
else:
    novoPreco = precoProduto + (precoProduto * 0.20)
    print('Seu preço sera de {}'.format(novoPreco))