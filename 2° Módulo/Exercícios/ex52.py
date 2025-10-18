# fazer um programa que vai ler um numero inteiro e vai dizer se ele é primo ou nao

n = int(input("digite um numero inteiro: "))

divisores = 0

for c in range(1, n+1):
    if n % c == 0:
        divisores += 1

if divisores == 2:
    print('Este numero é primo')
else:
    print('Este numero nao é primo')