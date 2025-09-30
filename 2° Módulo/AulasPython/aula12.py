nome = str(input("Qual é seu nome?"))
if nome == "joao":
    print('que nome lindo')
elif nome in 'pedro josé maria':
    print('belo nome')
else:
    print('que nome normal')
print('Tenha um bom dia {}'.format(nome))