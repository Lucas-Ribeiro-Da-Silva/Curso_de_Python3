"""
count - itertools
"""
from itertools import count

contador = count(start=5, step=2)

for valor in contador:
    print(round(valor,2))

    if valor >= 10:
        break

"""
from types import GeneratorType

variavel = zip('Alo', 'Alo')
print(list(variavel))

variavel = zip('Alo', 'Alo') #é iterador
print(next(variavel))
print(next(variavel))
print(next(variavel))

variavel = zip('Alo', 'Alo')
print(isinstance(variavel, GeneratorType))#não é gerador

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
print(isinstance(variavel, GeneratorType)) #é gerador

#range é um iteravel
"""