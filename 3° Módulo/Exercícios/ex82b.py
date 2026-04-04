#refazendo o exercicio 82 mas de outra forma

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N]: ').strip().lower()
    if resp == 'n':
        break

pares = []
impares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('-' * 40)

valores.sort()
pares.sort()
impares.sort()


print('Lista completa: ', end='')
for c in valores:
    print(c, end=' ')

print('\nOs valores pares foram: ', end='')
for p in pares:
    print(p, end=' ')

print('\nOs valores impares foram: ',end='')
for i in impares:
    print(i, end=' ')