"""
criar dois contadores usando algum laço for ou while

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2

ou seja, um crescente e outro decrescente

While é mais utilzado para coisas que não sabemos quando terá um fim, por isso o for é mais interessante aqui
"""

cont1 = 0
cont2 = 10

while cont1<=8 and cont2>=2:
    print(cont1, cont2)
    cont1+=1
    cont2-=1

########0u########################

#enumerate enumera cada volta do laço
#range faz a contagem iniciando em 10, terminando em 2, com passo -1
for progressivo,regressivo in enumerate(range(10, 1, -1)):
    print(regressivo, progressivo)



#enumerate enumera cada volta do laço
#range faz a contagem iniciando em 10, terminando em 2, com passo -1
for i in enumerate(range(10, 1, -1)):
    print(i)

