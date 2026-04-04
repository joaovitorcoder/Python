#vai ler varios numeros, guardar em uma lista
#vai mostrar quantos valores foram digitados
#vai mostrar a lista em ordem decrescente
#se o valor 5 esta ou nao na lista

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))

    res = input('Quer continuar [S/N]: ').strip().lower()
    if res == 'n':
        break

print(f'O total digitados na lista foi de {len(valores)} valores')

valores.sort(reverse=True)
print(F'Essa é a  lista em ordem decrescente: ', end='')
for i in valores:
    print(f'{i}', end=' ')

if 5 in valores:
    print(f'\nO valor 5 apareceu nas posições: ', end='')
    for indice, valor in enumerate(valores):
        if valor == 5:
            print(f'{indice}', end=' ')
else:
    print('\nO valor 5 não esta na lista!')