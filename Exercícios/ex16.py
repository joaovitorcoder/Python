#Crie um programa que leia um número real qualquer e mostra na tela a sua porção inteira
from math import trunc
numReal = float(input('Digite um numero: '))
numInt = trunc(numReal)
print('A parte inteira do número {:.2f} é {}'.format(numReal, numInt))