#fazer um programa que faça uma contagem regressiva de 10 a 0 com uma pausa de 1 segundo entre eles
import time

for c in range(10, -1, -1):
    time.sleep(1)#da 1 segundo de pausa entre um numero e outro
    print(c)
time.sleep(1)
print('Feliz ano novo!')