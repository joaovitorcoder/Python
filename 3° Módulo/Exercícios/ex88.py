# Crie um programa para gerar palpites da Mega-Sena.
#
# Requisitos:
# 1. Perguntar ao usuário quantos jogos ele deseja gerar.
# 2. Para cada jogo:
#    - Sortear 6 números aleatórios.
#    - Os números devem estar entre 1 e 60.
#    - Não pode haver números repetidos no mesmo jogo.
# 3. Armazenar cada jogo numa lista.
# 4. Guardar todos os jogos numa lista composta.
# 5. Mostrar todos os jogos gerados ao usuário.
from random import randint
from time import sleep

numerosSorteados = []
valores = []

quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(quantidadeJogos):

    #sorteando valores
    while len(valores) < 6:
        valor = randint(1, 60)

        if valor not in valores:
            valores.append(valor)

    valores.sort() # organiza os valores
    numerosSorteados.append(valores[:]) # faz uma cópia da lista
    valores.clear() # esvazia a lista


    print(f'Jogo {i + 1}: {numerosSorteados[i]}')
    sleep(0.5)