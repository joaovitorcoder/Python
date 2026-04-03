#Vai ler 5 valores, vai guarda-los dentro de uma lista, vai mostrar o menor e o maior valor e a suas respectivas posições na lista

valores = list()

for c in range(5):
    valores.append(int(input(f'Digite um valor: ')))

maior = menor = valores[0]
indiceMaior = indiceMenor = 0

print(f'Você digitou os valors: ', end='')

for indice, valor in enumerate(valores):
    if maior < valor:
        maior = valor
        indiceMaior = indice

    if menor > valor:
        menor = valor
        indiceMenor = indice

    print(valor, end=' ')


print(f'\nNa posição {indiceMaior} temos o maior valor {maior}')
print(f'Na posição {indiceMenor} temos o menor valor {menor}')