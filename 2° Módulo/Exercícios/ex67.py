calculoTabuada = resultado = 0

while calculoTabuada > -1:
    calculoTabuada = int(input('Você quer ver a tabuada de qual numero? '))
    if calculoTabuada < 0:
        print('Numero invalido, programa encerrado')
    else:
        for i in range (1, 11):
            resultado = calculoTabuada * i
            print('{} x {} = {}'.format(i, calculoTabuada, resultado))