#vai ler uma expressão qualquer que use parenteses, vai analisar a expressao e ver se ta com os parenteses abertos e fechados corretamente

while True:
    expressao = input('Digite uma expressão: ')
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')

    if len(pilha) == 0:
        print('Expressão válida')
    else:
        print('Expressão inválida')

    resp = input('Deseja verificar outra expressão? [S/N]: ').strip().lower()[0]
    if resp == 'n':
        break