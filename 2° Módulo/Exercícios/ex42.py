#ler 3 retas e mostrar se elas podem formar um triângulo, e mostrar qual triângulo pode ser formado

reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    if reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
        print('Um triângulo equilátero pode ser formado')
    elif reta1 == reta2 and reta1 != reta3 and reta2 != reta3 or reta1 != reta2 and reta3 != reta1 and reta2 == reta3 or reta1 == reta3 and reta1 != reta2 and reta2 != reta3:
        print('Um triângulo isósceles pode ser formado')
    else:
        print('Um triângulo escaleno pode ser formado')
else:
    print('Um triângulo não pode ser formado')