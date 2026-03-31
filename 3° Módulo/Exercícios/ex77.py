#crie um programa que tenha uma tupla com varias palavras(nao usar acentos ) depois disso
#mostre para cada palavra quais sao as suas vogais

palavras = ("acento", "aprender", "usar", "concerto", "trecho", "caminho", "raios", "clube", "flamengo", "cassio", "curso")


for p in palavras:
    print(f"\n{p.upper()} - ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")

#for p in palavras: - vai percorrer as palavras da tupla
#   for letras in p: - vai percorrer as letras de cada palavra
#       print(letra) - vai mostrar cada letra de cada palavra