#fazer um programa que leia um numero qualquer e mostre na tela seu fatorial

num = int(input('Digite um numero: '))
fatorial = 1
temp = num
while temp > 0:
    fatorial *= temp
    temp -= 1
print('O fatorial do numero {} é {}'.format(num, fatorial))

#Fazendo com o for ao inves do while
# fatorial = 1
# Calcularfatorial = num
# for c in range(1, Calcularfatorial + 1):
#     fatorial *= c
# print('O fatorial do numero {} é {}'.format(num, fatorial))