#Escreva um programa que calcule o aluguel de um carro com base na quilometragem rodada, cobrando 0.15 por km
#e cobrando 60 por dia

dias = float(input('Quantos dias alugado?'))
km = float(input('Quantos Km rodados?'))
porDia = dias * 60
porKm = km * 0.15
totalApagar = porKm + porDia
print('Total a pagar {}'.format(totalApagar))
