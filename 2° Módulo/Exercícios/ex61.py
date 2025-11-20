#ler o primeiro termo de uma PA e tambem a razao, e mostrar quais serao os 10 primeiros termos dessa PA,
#usando o while
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao dessa PA: '))
contador = 1
termos = primeiro_termo
while contador != 11:
    print('{}° termo é: {}'.format(contador, termos))
    termos += razao
    contador += 1
