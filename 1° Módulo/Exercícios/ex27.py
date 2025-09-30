#faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o ultimo nome
#separadamente
nome = input('Digite seu nome completo: ').strip()
nomeDividido = nome.split()
print('Seu primeiro nome é {} '.format(nomeDividido[0]))
print('Seu ultimo nome é {} '.format(nomeDividido[-1]))