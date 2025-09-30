#ler a idade de um jovem e informar se ele ainda vai se alistar, se é hora de se alistar, se ja
#passou do tempo de se alistar, também deverá informar o tempo que falta ou que passou do prazo

idade = int(input('quantos anos voce tem?'))

if idade > 18:
    print('Já passou do tempo de se alistar, passou {} anos do seu alistamento'.format(idade - 18))
elif idade == 18:
    print('É hora de se alistar!')
else:
    print('Você ainda vai se alistar, faltam {} anos para você se alistar'.format(18 - idade))

