#Faça um programa que leia uma frase pelo teclado
#mostre quantas vezes aparece a letra 'a'
#em que posição ela aparece a primeira vez
#em que posicao ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
ContandoA = frase.count('A')
primeiroA = frase.find('A')+1
ultimoA = frase.rfind('A')+1
print('Existe um total de {} letras A na frase'.format(ContandoA))
print('O primeiro A aparece na posicao {}'.format(primeiroA))
print('O ultimo A aparece na posicao {}'.format(ultimoA))
