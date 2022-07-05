"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symetric_difference ^ (elementos que estão nos dos sets, mas não em ambos)
"""

s1 = {1, 2, 3, 4, 5} #não tem keys e não tem indices
s1.add(6)

s2 = set()
s2.add(7)
s2.add((2, 3, 4, 'luiz'))
s2.discard(2)
s2.update('python')

#a diferença de add para uptade é que update va itear sobre cada elemento dele

l1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
l1 = set(l1)
l1 = list(l1)
print(l1)


s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6}
s5 = s3 | s4 #união
print(s5)
s5 = s3 - s4 #diferença
print(s5)
s5 = s3 ^ s4 #estão nos dois mas não estão ao mesmo tempo
print(s5)
s5 = s3 & s4 #intersecção
print(s5)