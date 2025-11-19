#fazer um programa que vai ler varios valores inteiros, vai imprimir a média entre eles, qual o maior, o menor
#e vai perguntar ao usuario se ele quer continuar a digitar valores ou nao

maior = -999999
menor = 999999
vezesRodadas = soma = media = 0
endPoint = 'S'
while endPoint == 'S':
    n = int(input('Digite um valor inteiro: '))
    soma += n
    vezesRodadas += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    media = soma / vezesRodadas
    if vezesRodadas == 10:
        endPoint = input('Voce deseja continuar a rodar o programa [S/N]: ').upper()

print('A média entre todos os valores digitados foi de {}\nO menor foi valor foi {}\n'
      'O maior valor foi {}'.format(media, menor, maior))