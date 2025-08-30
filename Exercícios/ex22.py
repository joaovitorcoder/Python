#crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# nome com todas as letras minusculas
#quantas letras ao todo (sem considerar espaços)
#quantas letra tem o primeiro nome

nome = str(input('Informe seu nome completo:')).strip()
nomeEmMaiusculo = nome.upper()#Transforma o nome em maiusculas
nomeEmMinusculo = nome.lower()#Transforma o nome em minusculas
qtdLetrassemEspacos = len(nome.replace(' ', ''))#Calcula quantidade de letras sem espaços
qtdLetras = len(nome.split()[0])#Calcula quantidade de letras do primeiro nome
print('Seu nome em maiusculas: {}'.format(nomeEmMaiusculo))
print('Seu nome em minusculas: {}'.format(nomeEmMinusculo))
print('Quantidade de letras que tem seu nome sem espaços: {}'.format(qtdLetrassemEspacos))
print('Quantidade de letras que tem seu primeiro nome: {}'.format(qtdLetras))
