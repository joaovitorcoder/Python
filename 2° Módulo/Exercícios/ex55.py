#fazer um programa que leia o peso de cinco pessoas e mostre qual foi o menor e qual é o maior

menor = 999
maior = -999
for c in range(1, 6):
    peso = float(input('Digite o peso das pessoas: '))
    if menor > peso:
        menor = peso
    if maior < peso:
        maior = peso
print('O menor peso encontrado foi {}, o maior foi de {}'.format(menor, maior))