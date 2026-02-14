calculoTabuada = resultado = 0

while True:
    calculoTabuada = int(input('Você quer ver a tabuada de qual numero? '))
    if calculoTabuada < 0:
        print('Numero invalido, programa encerrado')
        break
    for i in range (1, 11):
        resultado = calculoTabuada * i
        print(f'{i} x {calculoTabuada} = {resultado}')