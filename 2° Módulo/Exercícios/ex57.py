#vai ler o sexo de uma pessoa com M ou F, se o usuario digitar outra letra vai pedir para o usuario digitar novamente

sexo = 'J'
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o seu sexo [M/F]: ').upper()

if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'

print('Seu sexo é {}'.format(sexo))