#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados (versao str)
n = str(input('Digite um número de 0 a 9999: '))
numStr = n.strip()
milhar = numStr[0]
centenas = numStr[1]
dezenas = numStr[2]
unidades = numStr[3]
print('Milhar: {}'.format(milhar))
print('Centenas: {}'.format(centenas))
print('Dezenas: {}'.format(dezenas))
print('unidades: {}'.format(unidades))