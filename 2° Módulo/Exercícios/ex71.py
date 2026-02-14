#fazer um programa que simule um caixa eletronico no inicio, pergunte qual sera o valor a ser sacado(numero inteiro) e o programa
#vai informar quantas cedulas de cada valor serão entregues
#obs: considere que o caixa possui cedulas de 50, 20, 10 e 1. 999
cedula50 = cedula20 = cedula10 = cedula1 = resto = 0

print('-' * 30)
print('     CAIXA ELETRÔNICO     ')
print('-' * 30)

valor = int(input('Informe o valor a ser sacado: '))
for i in range(0, valor):
    if valor >= 50:
        cedula50 = valor // 50
        resto = valor - (cedula50 * 50)
    if resto >= 20:
        cedula20 = resto // 20
        resto -= (cedula20 * 20)
    if resto >= 10:
        cedula10 = resto // 10
        resto -= cedula10 * 10
    if resto >= 1:
        cedula1 = resto // 1
        resto -= cedula1 * 1

if cedula50:
    print(f'Você irá receber {cedula50} notas de 50')
if cedula20:
    print(f'Você irá receber {cedula20} notas de 20')
if cedula10:
    print(f'Você irá receber {cedula10} notas de 10')
if cedula1:
    print(f'Você irá receber {cedula1} notas de 1')
print('-' * 30)