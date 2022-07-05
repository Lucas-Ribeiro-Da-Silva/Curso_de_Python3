"""
zip - unindo iteraveis - só vai unir até a menor lista
zip_longest - itertools -
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

print(list(cidades_estados))

from itertools import zip_longest
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(cidades, estados, fillvalue ='Estado')
print(list(cidades_estados))

from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, cidades, estados)
for indice, cidade, estado in cidades_estados:
    print(indice, estado, cidade)
