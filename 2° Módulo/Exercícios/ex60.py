#fazer um programa que leia um numero qualquer e mostre na tela seu fatorial

num = int(input('Digite um numero: '))
fatorial = 1
temp = num

while temp > 0:
    fatorial *= temp
    temp -= 1
print('O fatorial do numero {} é {}'.format(num, fatorial))