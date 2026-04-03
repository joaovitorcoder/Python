# O usuario vai digitar varios valores, vou colocar eles em uma lista, caso ja exista nao adicione. No final serão exibidos todos os valores
#unicos digitados em ordem crescente

valores = list()
valorDigitado = 0

while True:
    valorDigitado = int(input('Digite um valor: '))


    if valorDigitado not in valores:
        valores.append(valorDigitado)
    else:
        print('Valor duplo! Não irei adicionar!')

    res = input('Deseja continuar? [S/N] ').strip().lower()
    if res == 'n':
        break

print('-'*40)

print('Os valores digitados foram: ', end='')
for i in valores:
    print(i, end=' ')