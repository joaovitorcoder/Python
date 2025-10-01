#criar um programa que vai ler duas notas e calcular a média, mostrando uma mensagem no final de acordo com a
#média atingida. Abaixo de 5.0 -> reprovado, média entre 5.0 e 6.9 -> recuperação,média 7.0 ou superior -> aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado!')
