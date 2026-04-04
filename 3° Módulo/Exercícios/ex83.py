#vai ler uma expressão qualquer que use parenteses, vai analisar a expressao e ver se ta com os parenteses abertos e fechados corretamente

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
            break

if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')