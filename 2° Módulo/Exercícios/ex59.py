
#criar um menu com somar,multiplicar, maior, novos numeros, sair do programa e o programa devera realizar
#a operação solicitada


contador = 0
operacao = 1
soma = 0
mult = 0
maior = -99999999999999999999999999999999
while operacao != 0:
    while contador <= 1:
        n = float(input('Digite um numero: '))
        soma += n
        mult *= n
        if n > maior:
            maior = n
        contador += 1
    operacao = int(input('Qual operação você deseja realizar\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Adicionar '
                         'novos numeros\n[0]Fechar o programa: '))
    if operacao == 3:
        print('O maior é {}'.format(maior))