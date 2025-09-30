#leia tres retas e escreva se elas podem ou nao formar um triangulo
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Um triângulo pode ser formado!')
else:
    print('Um triângulo não pode ser formado')