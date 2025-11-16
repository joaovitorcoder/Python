#o pc vai pensar em um numero entre 0 e 10 e o jogado vai jogar ate adivinhar e no final vai mostrar quantos palpites
#foram necessarios para o jogador acertar o numero

from random import randint
numeroAleatorio = randint(1, 10)

tentativas = 0
numeroDoJogador = 11

while numeroDoJogador != numeroAleatorio:
    numeroDoJogador = int(input('Digite um numero aleatorio de 0 a 10: '))
    tentativas += 1

print('Voce acertou!!!\nForam necessárias {} tentativas para voce acertar'.format(tentativas))