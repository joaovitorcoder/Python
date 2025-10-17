#calcular a soma entre todos os numeros impares que são multiplos de 3 e que se encontram entre 1 e 500
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print('A soma de todos os numeros impares e divisiveis por 3 entre 1 e 500 é {} '.format(s))