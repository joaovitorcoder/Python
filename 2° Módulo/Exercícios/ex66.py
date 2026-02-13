endPoint = 0
soma = numerosDigitados = 0
while endPoint != 999:
    numeros = int(input('Digite numero inteiro[CASO QUEIRA PARA DIGITE 999]: '))
    if numeros == 999:
        endPoint = 999
    else:
        numerosDigitados += 1
        soma += numeros
print('A soma dos {} numeros é de {}'.format(numerosDigitados, soma))