numeros = []
contador = primeiro3 = 0
for c in range(4):
    numeros.append(int(input(f'Digite um valor: ')))
tuplaValores = tuple(numeros)
print(f'Os valores digitados foram: {tuplaValores}')

numeros = []
for i in tuplaValores:
    if i == 9:
        contador += 1
    if i == 3:
        primeiro3 = tuplaValores.index(3) + 1
    if i % 2 == 0:
        numeros.append(i)
numerosPares = tuple(numeros)
del(numeros)
print('')

if contador:
    print(f'O numero 9 apareceu {contador} vezes')
else:
    print('Não apareceu o numero nove')

if primeiro3:
    print(f'O Valor 3 apareceu na posicao {primeiro3}')
else:
    print('Não apareceu o valor 3')

if numerosPares:
    print(f'Os numeros pares foram {numerosPares}')
else:
    print('Não apareceu valores pares')
