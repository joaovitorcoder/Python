#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequência

#No final mostre uma listagem de preços, organizando os dados em forma tabular

tupla = (
    "Lápis", 1.75,
    "Borracha", 2,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20
)

for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f"{tupla[item]:.<30}", end='')
    else:
        print(f"R${tupla[item]:>7.2f}")