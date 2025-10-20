#criar um programa que leia uma frase e diga se ela é um palindromo desconsiderando os espacos

frase = input('Digite aqui uma frase: ').replace(' ', '').lower()

invertida = ''

for i in range(len(frase) - 1, -1 , -1):
    invertida += frase[i]

if invertida == frase:
    print('É um palindromo')
else:
    print('Não é um palindromo')