a = input('digite qualquer coisa aqui ')
print('o tipo primitivo do que você digitou é ', type(a))
print(f'a variável é minúscula? {a.islower()}')
print(f'a variável é maiúscula? {a.isupper()}')
print(f'a variável é printável? {a.isprintable()}')
 #  este print abaixo verifica  se só tem ESPAÇO no conteúdo da variável, separado por virgula.      
print(f'a variável só tem espaços? {a.isspace()}')
print(f'é um numero? {a.isnumeric()}')
print(f'está capitalizada? {a.istitle()}')