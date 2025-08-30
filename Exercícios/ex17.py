#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa
from math import sqrt
catetoOposto = float(input('Informe o tamanho do cateto oposto: '))
catetoAdjacente = float(input('Informe o tamanho do cateto adjacente: '))
hipotenusaQuadrado = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)
hipotenusa = sqrt(hipotenusaQuadrado)
print('A hipotenusa mede {:.2f}'.format(hipotenusa))

#Solução do curso
#from math import hypot
#co = float(input('Digite o cateto oposto'))
#ca = float(input('Digite o cateto adjacente'))
#hi = hypot(co, ca)
#print('A hipotenusa mede {:.2f}'.format(hi))


