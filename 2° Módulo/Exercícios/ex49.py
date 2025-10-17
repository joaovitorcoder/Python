#fazer uma tabuada pedindo o numero para o usuario

n = int(input('Digite um numero: '))

for i in range(1, 11):
    valor = i * n
    print('{} X {} = {}'.format(i, n, valor))