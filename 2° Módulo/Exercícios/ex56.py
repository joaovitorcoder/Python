#fazer um programa que leia nome, idade, sexo de quatro pessoas e mostre:
#media das idades
#qual é o nome do homem mais velho
#quantas mulheres tem menos de vinte anos
media = 0
maiorIdade = -99999
menosDeVinte = 0
for c in range(4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite o sexo\n[1]Feminio\n[2]Masculino: '))

    media += idade / 4

    if sexo == 1:
        if idade < 20:
            menosDeVinte += 1


    if sexo == 2:
        if idade > maiorIdade:
            maiorIdade = nome


print('A média das idade é: {}'.format(media))
print('O homem de maior idade é: {}'.format(maiorIdade))
print('{} mulheres tem menos de vinte anos'.format(menosDeVinte))