#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados (versao int)
from math import trunc
num = float(input('Digite um numero de 0 a 9999: '))
numInt = trunc(num) #mesmo que o numero for decimal, tira a parte decimal, deixa apenas a parte inteira
milhar = numInt // 1000 #realiza a divisao inteira do numero, deixando apenas a casa dos milhar
centenas = (numInt // 100) %  10 #realiza a divisao inteira por 100, e depois pega somente o resto da div por 10, que é as centenas
dezenas = (numInt // 10) % 10 #realiza a divisao inteira por 10, e depois pega o resto da div por 10, que resulta na casa das dezenas
unidades = numInt % 10 #realiza a div de resto por 10 que resulta na casa das unidades
print('Milhar: {}'.format(milhar))
print('Centenas: {}'.format(centenas))
print('Dezenas: {}'.format(dezenas))
print('Unidades: {}'.format(unidades))










#9166 -> 9, uni -> 6