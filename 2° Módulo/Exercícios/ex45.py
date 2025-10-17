#criar um programa que faça o pc jogar jokenpo com vc (pedra, papel, tesoura)

from random import randint

escolha = input('Você escolhe pedra, papel ou tesoura: \n'
                '[ 1 ] Pedra \n'
                '[ 2 ] Papel\n'
                '[ 3 ] Tesoura\n'
                'Sua escolha: ')
if escolha == '1':
    escolha = 'pedra'
elif escolha == '2':
    escolha = 'papel'
else:
    escolha = 'tesoura'

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