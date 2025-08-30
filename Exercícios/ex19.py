#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice
nome1 = input('Digite o nome do primeiro: ')
nome2 = input('Digite o nome do segundo: ')
nome3 = input('Digite o nome do terceiro: ')
nome4 = input('Digite o nome do quarto: ')
lista = [nome1, nome2, nome3, nome4]
nomeRandom = choice(lista)#random.choice() -> escolhe um numero aleatorio em uma lista
print('O(a) {} foi o escolhido para apagar o quadro' .format(nomeRandom))