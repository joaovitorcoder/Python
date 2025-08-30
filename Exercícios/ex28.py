#Escreva um prgrama que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá  escrever na tela se o usuário venceu ou perdeu

from random import randint
numeroAleatorio = randint(0, 5)
numeroDoUsuario = int(input('Tente acertar o número: '))
if numeroDoUsuario == numeroAleatorio:
    print('Você acertou! PARABÉNS')
else:
    print('Você errou tente novamente! BURRO')