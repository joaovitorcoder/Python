#criar um programa que vai ler varios numeros ate 999 que é o numero para fechar o programa, o programa
#vai calcular a soma de todos os numeros sem contar o 999, e vai também contar quantos numeros foram colocados

somaNumeros = contador = 0
n = 1
print('Para para o programa digite 999')
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        contador += 1
        somaNumeros += n
print('O total de numeros digitados foi de {} e a soma entre eles foi de {}'.format(contador, somaNumeros))