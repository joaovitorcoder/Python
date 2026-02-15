#crie uma tupla com os 20 colocados da tabela do brasileirao na ordem de colocação depois mostre:
# - apenas os 5 primeiros colocados
# - os ultimos 4 colocados da tabela
# - uma lista com os times em ordem alfabetica
# - em que posição esta o time da chapecoense

times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo',
         'Botafogo', 'Corinthians', 'Grêmio', 'EC Vitória', 'Atlético-MG', 'Remo', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')
print('-'*30)
print(f'Os cincos primeiro da tabela:')
for i in times[:5]:
    print(f'{i}')
print('-'*30)

print('Os ultimos 4 colocados:')
for i in times[-4:]:
    print(f'{i}')
print('-'*30)

print('Tabela ordenada em ordem alfabetica:')
for i in sorted(times):
    print(f'{i}')
print('-'*30)

posicaoChapecoense = times.index('Chapecoense') + 1
print(f'O time da Chapecoense está na posição: {posicaoChapecoense}°')
print('-'*30)