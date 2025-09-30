#Faça um algoritmo que leia o valor de um sálario e mostre o salário com 15% de aumento
valorSal = float(input('Informe o sálario: '))
aumento = 0.15
SalComAumento = valorSal + valorSal * aumento
print('O valor do sálario com aumento é de {:.2f} reais'.format(SalComAumento))