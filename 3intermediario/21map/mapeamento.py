from dados import produtos, pessoas, lista
"""
nova_lista = map(lambda x: x * 2, lista)
#o mesmo resultado assim:
#nova_lista = [x * 2 for x in lista]
print(lista)
print(nova_lista)
print(list(nova_lista))
"""

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoas in nomes:
    print(pessoa)