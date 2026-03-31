#vai ler quatro numeros vai mostrar os quatros, vai retonar quantos noves tem, em qual posição apareceu o primeiro 3 e em os numeros pares
#digitados

numeros = (
    int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite o ultimo valor: ')),
)


print('os valores pares digitados foram: ', end='')
for j in numeros:
    print(j, end=" ")

print(f'\nTem {numeros.count(9)} numero nove') #retorna o tanto de numeros noves que tem na tupla

if 3 in numeros:
    print(f'O primeiro valor 3 apareceu na {numeros.index(3) + 1} posição')#retorna o index do primeiro numero 3 que apareceu na tupla
else:
    print('Nao tem valor 3 na lista')