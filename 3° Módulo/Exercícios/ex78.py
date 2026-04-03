#Vai ler 5 valores, vai guarda-los dentro de uma lista, vai mostrar o menor e o maior valor e a suas respectivas posições na lista

valores = list()
indiceMaior = list()
indiceMenor = list()

for c in range(5):
    valores.append(int(input(f'Digite um valor: ')))

maior = menor = valores[0]

print(f'Você digitou os valores: ', end='')


for indice, valor in enumerate(valores):
    if maior < valor:
        maior = valor
        indiceMaior = [indice]
    elif maior == valor:
        indiceMaior.append(indice)


    if menor > valor:
        menor = valor
        indiceMenor = [indice]
    elif menor == valor:
        indiceMenor.append(indice)

    print(valor, end=' ')


print(f'\nO maior valor digitado foi {maior} nas posições: ', end='')
for indice in indiceMaior:
    print(indice, end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for indice in indiceMenor:
    print(indice, end=' ')