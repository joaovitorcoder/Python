#um pg que tenha umma tupla total preenchida com uma contagem por extenso de zero ate vinte, seu pg devera ler um numero
#entre 0 e 20 pelo tecado e mostra-lo por extenso

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

numeroUser = int(input('Informe um numero entre 0 e 20: '))

if numeroUser < 0 or numeroUser > 20:
    while True:
        numeroUser = int(input('Tente novamente!! informe um numero entre 0 e 20: '))
        if numeroUser > 0 and numeroUser  <= 20:
            break
numeroExtenso = numeros[numeroUser]
print(f'O numero digitado foi {numeroExtenso}')