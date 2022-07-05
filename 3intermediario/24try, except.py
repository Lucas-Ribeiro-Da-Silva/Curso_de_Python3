"""
arquivo ......... linha
código
nome da excessão
"""

#tratamento geral, não é boa prática, o certo é tratar erros especificos
try:
    print(a)
except:
    print('Erro')

print('#' * 80)

try:
    print(b)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado.')
print('Mas bora continuar')

print('#' * 80)

try:
    c = []
    print(c[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado.')
print('Mas bora continuar..........')

print('#' * 80)

try:
    c = []
    print(c[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except IndexError as erro:
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
print('Mas bora continuar..........')

print('#' * 80)

try:
    d = {}
    print(d[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
print('Mas bora continuar..........')


print('#' * 80)

try:
    d = {}
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('código executado sem erros.')
    print(d)
print('Mas bora continuar..........')

print('#' * 80)

try:
    d = {}
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('código executado sem erros.')
    print(d)
finally:
    print('Finalmente é sempre executado')
print(d)
print('Mas bora continuar..........')