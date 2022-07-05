lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d = {x:y for x, y in lista}
print(d)
d1 = dict(lista)
print(d1)

#lembre-se, dictionay sem chave é um set
d2 = {x for x in range(5)}
print(d2, type(d2))

d3 = {f'chave_{x}': x**2 for x in range(5)}
print(d3, type(d3))