#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai
#perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#o empréstimo será negado.

ValorDaCasa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o valor do seu salário?'))
anos = int(input('Em quantos anos você vai pagar a casa?'))

anosCalculado = anos * 12

salarioCalculado = salario * 0.30 # calcula os 30% do salario

prestacao_mensal = anosCalculado / salarioCalculado

if prestacao_mensal > salarioCalculado:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')

