#crie um programa que tenha uma tupla com varias palavras(nao usar acentos ) depois disso
#mostre para cada palavra quais sao as suas vogais

palavras = ("acento", "usar", "concerto", "trecho", "caminho", "raios", "clube", "flamengo", "cassio")
vogais = "aeiou"
encontradas = []

#para cada palavra em palavras
for palavra in palavras:
    encontradas = [] #limpa a cada palavra

    for letra in palavra: #para cada letra na palavra
        if letra in vogais:#se a letra estiver em vogais
            encontradas.append(letra)#a lista recebe a letra

    print(f'{palavra} - {encontradas}')