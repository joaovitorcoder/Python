#programa que leia 2 numeros e compareos, falando qual é o maior ou se eles forem iguais o programa
# vai falar tambem

n1 = float(input('Digite o 1° valor'))
n2 = float(input('Digite o 2°valor'))

if n1 > n2:
    print('O 1° valor é maior que o 2°')
elif n2 > n1:
    print('O 2° valor é maior que o 1°')
else:
    print('Os dois valores são iguais')