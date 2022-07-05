"""
estou criando um arquivo txt
escrevendo 3 linhas nele
e fechando o mesmo


W+ escreve, apaga o que tinha no arquivo para escrever em cima
r+ lê
a+ acrescenta coisas no fim do doc
"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linha: ')
print(file.read())
print('###################')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('###################')

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()


"""
para outras linguagens:

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()
"""

"""
O jeito certo de fazer em python:

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())
    
"""

import os
os.remove('abc.txt')