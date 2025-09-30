#Faça um algoritmo que leia o preço de um produto e calcule seu novo preço com 5% de desconto
preco = float(input('Informe o preço do produto: '))
desc = 0.05
precoComDesc = preco - preco * desc
print('O preço com desconto é de {:.3f} reais'.format(precoComDesc))