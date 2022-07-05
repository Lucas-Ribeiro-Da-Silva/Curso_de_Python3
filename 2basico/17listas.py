"""
listas
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

"""
existem tipos de dados, int, boolean, float.... contudo,
estes dados armazenam um só valor
as listas sao como um novo tipo de dado, o qual armazena varios valores

texto = 'valor'
lista = [1, 2, 3, 4, 'Luiz', True]
"""

lista = ['A', 'B', 'C', 'D', 'E']
string = 'ABCDE'
lista[4] = 'qualquer coisa'
print(string[1])
print(lista[1])
print(lista)
print(lista[-1])
print(lista[0:3])
print(lista[::2])
print(lista[::-1])


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)


l1 = [1, 2, 3]
l2 = [4, 5,6]
l1.extend(l2)
l1.extend('a')
print(l1)

l1 = [1, 2, 3]
l2 = [4, 5,6]
l1.extend(l2)
print(l1)

l1 = [1, 2, 3]
l2 = [4, 5,6]
l1.extend('a') #extend concatena valores ou listas
print(l1)

l1 = [1, 2, 3]
l2 = [4, 5,6]
l1.append('b') #append insere valores no fim da lista
print(l1)

l1 = [1, 2, 3]
l2 = [4, 5,6]
l1.insert(0, 'banana') #insert insere valores na posição indicada pelo indice
print(l1)

l2 = [4, 5,6]
print(l2)
l2.insert(0, 'banana') #insert insere valores na posição indicada pelo indice
print(l2)
l2.pop() #pop exclui o ultimo item da lista
print(l2)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3)
del(l3[3:5]) #del deleta valores especificos
print(l3)

print(max(l3))
print(min(l3))


l4 = range(1, 100)
print(l4)

l4 = list(range(1, 100, 8))
print(l4)

l5 = list(range(0, 11))

for valor in l5:
    print(valor)
