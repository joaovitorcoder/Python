#O programa vai perguntar se o usuario quer que seja mostrado mais termos, e ele vai encerrar quando o usuario digitar n na pergunta

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
fimContagem = 10
contador = 1
while contador <= fimContagem:
    print('{}° termo da PA: {}'.format(contador, primeiroTermo))
    primeiroTermo += razao

    if contador == fimContagem:
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

        if pergunta == 'S':
            termos = int(input('Quantos termos deseja mostrar: '))
            fimContagem += termos
        elif pergunta == 'N':
            print('A contagem foi finalizada com {} termos mostrados'.format(contador))
            break

    contador += 1