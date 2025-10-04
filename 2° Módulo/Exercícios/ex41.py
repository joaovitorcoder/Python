#ler a idade dos alunos de uma escola de natacao e indicar sua categoria
#ate 9 anos - mirim
#ate 14 anos - infantil
#ate 19 anos - junior
#ate 20 anos - senior
#acima - master

idade = int(input('Informe a idade do aluno: '))

if idade <= 9:
    print('Aluno de categoria MIRIM')
elif idade <= 14:
    print('Aluno de categoria INFANTIL')
elif idade <= 19:
    print('Aluno de categoria JUNIOR')
elif idade <= 20:
    print('Aluno de categoria SENIOR')
else:
    print('Aluno de categoria MASTER')