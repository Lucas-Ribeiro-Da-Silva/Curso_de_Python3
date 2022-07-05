"""
pass = comando para quando não sabemos o que escrver pular a execução da instrução
...  = reticencias faz a mesma coisa
"""

valor = False
valor1 = True

if valor:
    pass
else:
    print('alguma coisa')

if valor1:
    pass
else:
    print('alguma coisa')

if valor:
    ...
else:
    print('...tmb funciona')

if valor1:
    ...
else:
    print('...tmb funciona')