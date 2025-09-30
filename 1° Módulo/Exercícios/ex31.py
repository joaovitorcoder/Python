#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50
#por km para viagens de até 200km e R$0.45 para viagens mais longas
distancia = float(input('Digite a distância (em Km/h): '))
if distancia <= 200:
    pagamento = distancia * 0.50
else:
    pagamento = distancia * 0.45
print('O preço da passagem será de R${}'.format(pagamento))