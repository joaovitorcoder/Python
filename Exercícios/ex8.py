#Faça um programa que leia um valor em metros,
#e o escreva convertido em centimetros e milimetros

valorMetros = float(input('Digite um valor (em metros): '))
valorCentimetros = valorMetros * 100
valorMilimetros = valorCentimetros * 10

print('Seu valor em centímetros é {} e seu valor em milímetros é {}'.format(valorCentimetros, valorMilimetros))