#fazer um programa que peça seis numeros inteiros e que devolva a soma somente dos numeros pares
s = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print('A soma de todos os numeros pares digitados foi {}'.format(s))