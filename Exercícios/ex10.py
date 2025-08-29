#Faça um programa que receba um valor em dinheiro e converta esse valor para dólares, considere: US$1,00 = R$3,27

nReais = float(input('Digite a quantidade a ser convertida: '))
nDolares = nReais / 3.27

print('Você podera comprar {:.2f} dólares'.format(nDolares))