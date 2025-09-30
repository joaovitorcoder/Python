#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
#ele foi multado. A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Digite a velocidade em que o carro estava: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = 7 * (velocidade - 80)
    print('O valor da multa é de {}'.format(multa))
else:
    print('Velocidade boa! Siga em frente, com cuidado')