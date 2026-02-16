from random import randint
numeros = []

for i in range(5):
    numeros.append(randint(1, 10))
tuplaNumeros = tuple(numeros)
del(numeros)
menor = tuplaNumeros[0]
maior = tuplaNumeros[-1]

for j in tuplaNumeros:
    if j < menor:
        menor = j
    if j > maior:
        maior = j

print(f'Os valores sorteados foram: {tuplaNumeros}')
print(f'O maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')