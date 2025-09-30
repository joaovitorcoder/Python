n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('Sua média foi boa!' if m >= 6 else 'Sua média foi ruim!') #Condição if, else simplificada em somente uma linha