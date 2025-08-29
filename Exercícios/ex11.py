#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m^2

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a  altura da parede: '))
area = altura * largura
quantidadeNecessaria = area/2
print('A quantidade necessária de tinta sera {}L'.format(quantidadeNecessaria))