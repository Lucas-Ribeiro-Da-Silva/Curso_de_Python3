"""
tupla não pode ser modificada, nem indice nem valor nem chave
mas pode ser convertida em lista com .list
"""

t1 = (1, 2, 3, 'a', 'Luiz') #não é obrigatório parentesis
print(t1, type(t1))

t2 = 1,
print(t2, type(t2))

t3 = 1, 2, 3, 4, 5
print(t3, type(t3))
t3 = list(t3)
t3[1] = 'alterado'
print(t3, type(t3))
t3 = tuple(t3)
print(t3, type(t3))

