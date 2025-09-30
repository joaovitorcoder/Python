#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'Santo'
cidade = input('Digite o nome de uma cidade: ').strip()
cidadeDividida = cidade.lower().split()
if(cidadeDividida[0] == 'santo'):
    print('Sua cidade começa com o nome Santo!')
else:
    print('Sua cidade não começa com o nome Santo')