#criar um programa que faça o pc jogar jokenpo com vc (pedra, papel, tesoura)

from random import randint

escolha = input('Você escolhe pedra, papel ou tesoura: ')
nAleatorio = randint(1, 3)
if nAleatorio == 1:
    escolhaPC = 'pedra'
elif nAleatorio == 2:
    escolhaPC = 'papel'
else:
    escolhaPC = 'tesoura'

if escolha == 'pedra' and escolhaPC == 'pedra':
    print('Empate')
elif escolha == 'pedra' and escolhaPC == 'papel':
    print('Você perdeu')
elif escolha == 'pedra' and escolhaPC == 'tesoura':
    print('Você ganhou')
elif escolha == 'papel' and escolhaPC == 'pedra':
    print('Você ganhou')
elif escolha == 'papel' and escolhaPC == 'papel':
    print('Empate')
elif escolha == 'papel' and escolhaPC == 'tesoura':
    print('Você perdeu')
elif escolha == 'tesoura' and escolhaPC == 'pedra':
    print('Você perdeu')
elif escolha == 'tesoura' and escolhaPC == 'papel':
    print('Você ganhou')
elif escolha == 'tesoura' and escolhaPC == 'tesoura':
    print('Empate')

print('Escolha do computador: {}'.format(escolhaPC))