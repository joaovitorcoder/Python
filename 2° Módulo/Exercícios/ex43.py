#ler o peso e altura de uma pessoa, calcular imc e mostrar seu status
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#25 ate 30: sobrepeso
#30 ate 40: obesidade
#acima de 40: obesidade morbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura ** 2)
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você esta no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você esta sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você esta obeso')
else:
    print('Você tem obesidade mórbida')