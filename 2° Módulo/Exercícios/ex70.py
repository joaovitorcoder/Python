#crie um programa que leia o nome e o preço de vários produtos, o programa deverá perguntar se o usuário quer ou
#não continuar,no final, mostre:
# - Qual o total gasto na compra
# - Quantos produtos custam mais de R$1000
# - Qual é o nome do produto mais barato
total = produtosMaioresde1000 = 0
produtoMaisCaro = 99999
print('-'*30)
print('     CADASTRO DE PRODUTOS     ')
print('-'*30)

while True:
    nomeProduto = input('Qual o nome do produto: ').replace(' ', '').capitalize()
    precoProduto = float(input('Qual o valor do produto: '))

    total += precoProduto
    if precoProduto > 1000:
        produtosMaioresde1000 += 1
    if precoProduto < produtoMaisCaro:
        produtoMaisCaro = precoProduto
        nomeProdutoMaisBarato = nomeProduto

    resp = str(input('Quer continuar? [S/N] ')).replace(' ', '').lower()[0]
    if resp == 'n':
        break

print(f'Total dos produtos: {total}')
print(f'Qunatidade de produtos maiores de R$ 1000: {produtosMaioresde1000}')
print(f'O nome do produto mais barato é: {nomeProdutoMaisBarato}')