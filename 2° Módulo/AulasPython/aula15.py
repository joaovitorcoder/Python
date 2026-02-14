#Se o True for colocado dentro da condição do while o bloco vai ser executado pra sempre,pra fazer esse loop para tem que adicionar o comando
#break
n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# print('a soma vale {}'.format(s))
print(f'A soma vale {s}')