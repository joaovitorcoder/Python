#crie um programa que tenha uma tupla com varias palavras(nao usar acentos ) depois disso
#mostre para cada palavra quais sao as suas vogais

palavras = ('acento', 'usar')#, "usar", "concerto", "trecho", "caminho", "raios", "clube", "flamengo", "cassio")
vogais = "aeiou"
encontradas = []

for letra in palavras:
    if letra in vogais and letra not in encontradas:
        encontradas.append(letra)

print(f"{palavras} - {encontradas}")