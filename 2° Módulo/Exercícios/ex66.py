
soma = numerosDigitados = 0
while True:
    numeros = int(input('Digite numero inteiro[CASO QUEIRA PARA DIGITE 999]: '))
    if numeros == 999:
        break
    numerosDigitados += 1
    soma += numeros
print(f'A soma dos {numerosDigitados} números é de {soma}')