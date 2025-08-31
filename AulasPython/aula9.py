frase = 'Curso em Video Python'
#print(frase.upper().count('O')) Pega a frase joga pra maiusculas e conta quantos 'O' maiusculos tem
#print(len(frase.strip())) Vai remover os espaços do começo e do fim, e vai devolver o tamanho da frase
#print(frase.replace('Python', 'Android')) vai trocar a palavra Python pela palavra android
#print('Curso' in frase) verifica se a palavra curso esta dentro da frase, e devovle True porque tem a palavra
#print(frase.find('Curso')) vai verificar se na frase ha a palavra curso e vai devolver o indice da primeira letra da palavra, no caso 0
#print(frase.lower().find("video")) vai verificar se na frase ha a palavra video e vai devolver o indice (na frase totalmente em minusculas)
dividido = frase.split()
print(dividido[0][0]) # vai pegar a frase, vai dividi-la em modulos, vai pegar o primeiro modulo, e vai pegar a primeira letra do primeiro modulo, nesse caso "C"




# print('Oi')
#
# print('''Lorem ipsum dolor sit amet.
# Ut quidem repudiandae et internos cumque
# 33 aspernatur soluta id maiores maxime aut
# unde molestiae rem tempora tenetur et dolore modi.
# Non saepe dicta qui placeat ipsa aut impedit nostrum.
# Ut inventore facere est amet adipisci id rerum sunt
# eos quia dignissimos eum animi nobis aut aliquam velit?
# ic quos minus eum doloremque cumque ut quaerat ipsa in
# galisum quasi aut dolores delectus ut amet
# molestiae in voluptatibus reprehenderit?
# In voluptatum explicabo qui error minima et quia numquam
# aut aperiam vero eum deleniti doloremque et doloribus soluta
# non earum voluptatem. Aut quisquam sunt ut temporibus sapiente
# rem voluptatem tempora.''') # vai mostrar o texto completo em um unico print