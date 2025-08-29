#Faça um programa que leia graus celsius e o escreva convertendo para graus fahrenheit

celsius = float(input('Digite a temperatura °C'))
fahrenheit = celsius * (9/5) + 32
print('A temperatura em graus fahrenheit é de {}°F'.format(fahrenheit))