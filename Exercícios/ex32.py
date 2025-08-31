#faça um programa que leia um ano e mostre se esse ano é bissexto ou não
from datetime import date
ano = int(input('Digite o ano a ser verificado, coloque 0 para verificar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de{} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))