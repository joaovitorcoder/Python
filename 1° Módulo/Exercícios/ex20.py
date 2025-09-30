#Um professor quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada

from random import shuffle
nome1 = input('Digte o 1° nome: ')
nome2 = input('Digite o 2° nome: ')
nome3 = input('Digite o 3° nome: ')
nome4 = input('Digite o 4° nome: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista) #embaralha a lista
print('A ordem sorteada foi:')
print(lista)
