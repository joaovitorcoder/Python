#leia um numero inteiro q peça para o usuario escolher qual sera a base de conversao - 1 binario - 2 octal
#3 hexadecimal

num = int(input('Digite um número inteiro: '))

escolha = int(input('Você deseja converter para \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n'))

if escolha == 1:
    binario = bin(num)[2:]
    print('Seu número em binário: {}'.format(binario))
elif escolha == 2:
    octal = oct(num)[2:]
    print('Seu número em octal: {}'.format(octal))
elif escolha == 3:
    hexadecimal = hex(num)[2:]
    print('Seu número em hexadecimal: {}'.format(hexadecimal))
else:
    print('Escolha invalida, tente novamente')