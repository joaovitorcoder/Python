#criar um programa que leia o ano de nascimento de 7 pessoas. e no final mostra
#quantas sao de maior e quantas nao


deMaiores = 0
deMenores = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        deMaiores += 1
    else:
        deMenores += 1
print("{} pessoas são de maiores, {} pessoas são de menores".format(deMaiores, deMenores))