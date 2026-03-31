from random import randint
numeros = []

for i in range(5):
    numeros.append(randint(1, 10))
tuplaNumeros = tuple(numeros) #transforma em tupla
del(numeros)
menor = tuplaNumeros[0]
maior = tuplaNumeros[-1]

for j in tuplaNumeros:
    if j < menor:
        menor = j
    if j > maior:
        maior = j

print(f'Os valores sorteados foram: ', end='')
for i in tuplaNumeros:
    print(f'{i} ', end='')
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')