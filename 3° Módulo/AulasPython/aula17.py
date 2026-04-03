# num = [2, 5, 9, 1]
# num[2] = 3 # Troca o valor do indice dois para 3
# num.append(7)# Adiciona o 7 a lista
# num.sort(reverse=True) # Organiza a lista
# num.sort(reverse=True) Organiza a lista em ordem decrescente
# num.insert(2, 2) # Adiciona o numero 0 no indice dois
# num.pop(2)  Vai remover o elemento do indice dois
#if 5 in num:
#    num.remove(5) # Remove o primeiro elemento passado como parâmetro
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

# valores = list() # Declara uma lista do mesmo jeito que os colchetes fazem

# for cont in range (5):
#     valores.append(int(input('Digite um valor: ')))

# enumerate(valores) Pega o valor do indice


# for indice, valor in enumerate(valores):
#     print(f'Na posição {indice}, temos o valor {valor}')
# print('Cheguei ao final da lista')

a = [2, 3, 4, 6]
b = a[:] # B vai receber uma cópia de A dentro de B
b [2] = 8
print(a)
print(b)