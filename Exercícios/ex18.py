#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seu seno, cosseno e tangente
import math
ang = float(input('Informe um ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno desse ângulo vale {:.3f}\nO cosseno vale {:.3f}\nA tangente vale {:.3f}'.format(seno, cosseno, tang))