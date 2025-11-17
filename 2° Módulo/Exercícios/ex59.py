
#criar um menu com somar,multiplicar, maior, novos numeros, sair do programa e o programa devera realizar
#a operação solicitada
maior = -99999999999999

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
soma = n1 + n2
mult = n1 * n2
if n1 > n2:
    maior = n1
else:
    maior = n2


operacao = 2

while operacao != 0:
    operacao = int(input('Qual operação você deseja realizar\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Adicionar '
                         'novos numeros\n[0]Fechar o programa: '))

    if operacao == 1:
        print('A soma é {}'.format(soma))
    elif operacao == 2:
        print('A multiplicacao é {}'.format(mult))
    elif operacao == 3:
        print('O maior numero é {}'.format(maior))
    elif operacao == 4:
        n = float(input('Digite outros numeros: '))
        soma += n
        mult *= n
        if n > maior:
            maior = n