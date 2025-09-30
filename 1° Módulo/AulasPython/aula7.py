#A potencia pode ser feita utilizando o operador de potencia (**)
#ou então a função interna da potencia pow(4,2) = 16

#Pra achar o quadrado de um numero é utilizado x**(1/2) = y
#ou seja, eleva o numero a meio que é a mesma coisa que
#que tirar a raiz quadrada, e os parenteses obrigam o python
#calcular primeiro o 0,5 que é 1/2
#Caso quiser calcular a raiz cubica de um numero é facil, só
#usar a formula x**(1/3) = y, elevar a 1/3 é a mesma coisa que
#tirar a raiz cubica

#nome = input('Digite seu nome: ')
#print('Prazer em te conhecer {:20}!' .format(nome))
#O :20 no meio das chaves faz com que o nome seja
#escrito em 20 caracteres, independente de quantos caracteres que tiver o nome
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma é {}, o produto é {}, e a divisão é {:.3f} ' .format(s, m, d), end='')#":.3f" dentro das chaves formata o valor dentro das chaves para 3 casas flutuantes (decimais)
print('Divisão inteira é {}, e potência é {}'.format(di, e))