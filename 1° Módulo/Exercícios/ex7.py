#Faça um programa que leia as duas notas de um aluno e mostre sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('A média do aluno foi de: {:.1f}'.format(media))