#um programa que jogue par ou impar com o pc, o jogo só sera interrompido quando o jogador perder, mostrando o total de vitorias
#consecutivas que ele conquistou ao final da partida

from random import randint
vitorias = 0

while True:
    numeroUser = int(input('Escolha um numero: '))
    escolhaUser = input('Escolha entre par ou impar: ').lower().replace(' ', '')[0]
    numeroPC = randint(0, 1000)
    if (numeroPC + numeroUser) % 2 == 0:
        parOuImpar = 'PAR'
    else:
        parOuImpar = 'IMPAR'
    print(f'Numero jogado pelo PC: {numeroPC}, a soma resulta em {numeroPC + numeroUser} que é {parOuImpar}')
    if (numeroUser + numeroPC) % 2 == 0 and escolhaUser == 'p':
        print('Você acertou!! Parabéns + 1 vitória')
        vitorias += 1
    else:
        print(f'Você errou, teve {vitorias} vitorias consecutivas')
        break