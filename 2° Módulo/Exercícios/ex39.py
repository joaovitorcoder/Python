#ler a idade de um jovem e informar se ele ainda vai se alistar, se é hora de se alistar, se ja
#passou do tempo de se alistar, também deverá informar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year #pega o ano atual

sexo = input('Você é homem ou mulher? ')

if sexo == 'homem':
    nasc = int(input('Ano de seu nascimento?'))
    idade = atual - nasc
    print('Você tem {} anos'.format(idade))
    if idade > 18:
        print('Já passou do tempo de se alistar, passou {} anos do seu alistamento'.format(idade - 18))
    elif idade == 18:
        print('É hora de se alistar!')
    else:
        print('Você ainda vai se alistar, faltam {} anos para você se alistar'.format(18 - idade))
else:
    print('Você não precisa se alistar por ser mulher!')
