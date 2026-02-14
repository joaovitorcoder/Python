#crie um programa que leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
#não continuar,no final, mostre:
# - quantidade de pessoas que tem mais de 18 anos
# - quantos homens foram cadastrados
# - quantas mulheres tem menos de 20 anos
pessoasMaiores = quantidadeHomens = mulheresMenosDe20 = 0

print('-'*30)
print('     CADASTRO DE PESSOAS     ')
print('-'*30)

while True:
    idade = int(input('Insira a idade: '))
    sexo = input('Insira o sexo [M/F]: ').lower().replace(' ', '')[0]

    if idade > 18:
        pessoasMaiores += 1
    if sexo == 'm':
        quantidadeHomens += 1
    if sexo == 'f' and idade < 20:
        mulheresMenosDe20 += 1

    resp = input('Quer continuar? [S/N]').lower().replace(' ', '')[0]

    if resp == 'n':
        break

print(f'Quantidade de pessoas maiores de 18: {pessoasMaiores}')
print(f'Quantidade de homens cadastrados: {quantidadeHomens}')
print(f'Quantidade de mulheres menores de 20: {mulheresMenosDe20}')