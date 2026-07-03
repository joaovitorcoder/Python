# Crie um programa que leia o nome e duas notas de vários alunos, ao final mostre o boletim contendo a média de cada um
# dos alunos, e permita que o usuario veja o boletim por aluno individualmente.

valores = []
alunos = []

while True:
    nome = str(input('Nome do aluno: '))

    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2

    valores.append(nome)
    valores.append(nota1)
    valores.append(nota2)
    valores.append(media)

    alunos.append(valores[:])
    valores.clear()

    resp = input('Deseja cadastrar outro aluno? [S/N] ').upper()[0]
    if resp == 'N':
        break

print()

for j in range(len(alunos)):
    print(f'Aluno {j + 1}: {alunos[j][0]}')
    print(f'Nota 1: {alunos[j][1]}')
    print(f'Nota 2: {alunos[j][2]}')
    print(f'Média: {alunos[j][3]}')
    print()

while True:
    boletim = int(input('Deseja consultar o boletim de qual aluno?[ 999 - Sair ] '))


    if boletim == 999:
        break
    boletim -= 1
    if 0 <= boletim < len(alunos):
        print(alunos[boletim])
    else:
        print('Indice invalido')