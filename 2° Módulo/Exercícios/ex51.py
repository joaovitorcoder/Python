# fazer um programa que vai pedir a razao de uma PA e o primeiro termo, vai mostrar os 10 primeiros termos dessa PA

primeiroTermo = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a razao dessa PA: '))
Termos = primeiroTermo
for c in range(1, 11):
    print('{}° termo {}'.format(c, Termos))
    Termos += Razao