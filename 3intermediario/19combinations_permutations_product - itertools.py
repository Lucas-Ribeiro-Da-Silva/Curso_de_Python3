"""
combinations - combinação - ordem não importa
permutations - permutação - ordem importa
ambos não repetem valores únicos
Product - Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabicio', 'Rose']
for grupo in combinations(pessoas, 2):
    print(grupo)

print('#' * 80)

pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabicio', 'Rose']
for grupo in permutations(pessoas, 2):
    print(grupo)

print('#' * 80)

pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabicio', 'Rose']
for grupo in product(pessoas, repeat=2):
    print(grupo)