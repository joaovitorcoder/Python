a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))
print('É numerico: ', a.isnumeric())
print('É alfanumerico: ', a.isalnum())
print('É alfabetico: ', a.isalpha())
print('Esta em maiusculo: ', a.isupper())
print('Esta em minusculo: ', a.islower())
print('Só tem espaços? ', a.isspace())
print('Está capitalizada? ', a.istitle())

# Faça um programa que leia algo dentro de uma variavel e 
# exiba tudo sobre a variavel, "secando a variavel".