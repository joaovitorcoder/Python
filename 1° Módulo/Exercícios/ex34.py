#escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento
#para salários superiores a R$1250.00, calcule um aumento de 10%, para inferiores ou iguais o aumento é de 15%
salario = float(input('Digite o salário: '))
if salario > 1250.00:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)
print('O reajuste do seu salário foi de {}'.format(aumento))