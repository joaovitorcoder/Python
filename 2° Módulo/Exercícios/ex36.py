#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai
#perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#o empréstimo será negado.

ValorDaCasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o valor do seu salário?'))
anos = int(input('Em quantos anos você vai pagar a casa?'))

prestacao_mensal = ValorDaCasa / (anos * 12)

print('A prestação será de R${:.2f}'.format(prestacao_mensal))

if prestacao_mensal <= (salario * 0.30):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')

