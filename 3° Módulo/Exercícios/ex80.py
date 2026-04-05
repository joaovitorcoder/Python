#Um programa que vai ler cinco valores numericos, e os cadastre em uma lista ja na posição correta de inserção, sem usar o sort
# No final mostre a lista na tela em ordem, 5, 2, 8, 1, 3

valores = []
maior = menor = 0

for i in range(5):
    valor = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(valor)
        print('Adicionando o valor ao final da lista...')
        maior = valor
    elif maior > valor:
        print('Adicionando na posição 0 da lista...')
        valores.insert(0, valor)
        menor = valor
    elif maior < valor:
        print('Adicionando o valor ao final da lista...')
        valores.append(valor)
        maior = valor
