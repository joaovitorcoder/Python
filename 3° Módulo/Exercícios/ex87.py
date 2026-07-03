# aprimore o desafio anterior, mostrando no final:
# a ) A soma de todos os valores pares digitados
# b ) A soma dos valores da terceira coluna
# c ) O maior valor da segunda linha

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
          ]

for linha in range(len(matriz)): # percorre todas as linhas da matriz, no caso 0, 1 ,2
    for coluna in range(len(matriz[linha])): # no valor da linha atual, percorre todas as colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print()

# printando os valores da matriz

soma_valores = 0
somaValoresTerceiraColuna = 0
maiorValor = 0

for linha in range(len(matriz)):

    if linha == 1:
        maiorValor = max(matriz[linha])

    for coluna in range(len(matriz[linha])):

        if matriz[linha][coluna] % 2 == 0:
            soma_valores += matriz[linha][coluna]

        print(f'[{matriz[linha][coluna]:^3}]', end='')

        if coluna == 2:
            somaValoresTerceiraColuna += matriz[linha][coluna]

    print()

print('-' * 80)

print(f'A soma de todos os valores pares da matriz é de: {soma_valores}')
print(f'A soma dos valores da terceira coluna é de: {somaValoresTerceiraColuna}')
print(f'O maior valor da segunda linha é de: {maiorValor}')

