lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))
lista = 12345
print(hasattr(lista, '__iter__')) #iter é iteravel
lista = 'string'
print(hasattr(lista, '__iter__'))

#o laço for tansforma a lista em um iterador
lista = [0, 1, 2, 3, 4, 5]
for v in lista:
    print(v)

print(hasattr(lista, '__next__')) #next é iterável

lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

import sys
lista = list(range(10))
print(sys.getsizeof(lista))#quantos bytes ocupa isso
lista = list(range(100))
print(sys.getsizeof(lista))#quantos bytes ocupa isso


import sys
import time
def gera():
    r=[]
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r
g = gera()
for v in g:
    print(v)


import sys
import time
def gera1():
    for n in range(100):
        yield n
        time.sleep(0.1)
g = gera1()
print(g)

for v in g:
    print(v)

import sys
l1 = [x for x in range(1000)]
print(type(l1)) #list
print(sys.getsizeof(l1)) #consome muita memoria guardando os valores 
l2 = (x for x in range(1000))
print(type(l2)) #generator
print(sys.getsizeof(l2)) #a memoria é sempre igual


