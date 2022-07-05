"""
funções lambda(funções anônimas)
"""

a = lambda x, y: x * y
print(a(2, 2))

#essa função equivale a:
def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)
print(var)

#############################

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)
#########################################
lista1 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista1.sort(key=lambda item: item[1], reverse=True)
print(lista1)

################################################
lista2 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista2))
###################################################
lista3 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1], reverse=True))