#vai criar uma matriz 3x3 e vai preencher com os valores lidos pelo teclado
#no final vai mostrar a matriz na tela com a formatação correta

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
          ]

for linha in range(len(matriz)): # percorre todas as linhas da matriz, no caso 0, 1 ,2
    for coluna in range(len(matriz[linha])): # no valor da linha atual, percorre todas as colunas
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))


# printando os valores da matriz

print(f'{"-" * 30} valores da matriz {"-" * 30}')

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
    print()
print('-' * 80)


