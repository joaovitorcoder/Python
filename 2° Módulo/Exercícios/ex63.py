#leia o valor n que é inteiro e o programa vai ter que mostrar os n primeiros valores da sequencia de
#Fibonacci
a = prox = 0
b = 1
contador  = 0
n = int(input('Digite um numero inteiro: '))
while contador != n:

    print(a)
    prox = a + b
    a = b
    b = prox
    contador += 1
