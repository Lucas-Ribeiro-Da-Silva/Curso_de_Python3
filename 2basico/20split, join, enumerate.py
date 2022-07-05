"""
split = dividir uma string
join = juntar uma lista
enumerate = enumerar elementos da lista #iteraveis
"""

string = "O Brasil é o país do futebol"
lista_1 = string.split(" ")
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')#.count conta quantas vezes cada palavr aparece na frase


string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(" ")
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')



string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(" ")  #.split divide uma string gerando uma lista
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())#.strip remove espaços do inicio e do fim, capitalize deixa a primeira maiuscula


string = 'O Brasil é penta'
lista = string.split(' ')
string2 = ','.join(lista) #join junta elementos de uma lista

print(string)
print(lista)
print(string2)


###################################### os dois codigos a seguir fazem a mesma coisa

lista = ['LUiz', 'Joao', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

lista = [
    [0, 'Luiz'],
    [1, 'Joao'],
    [2, 'Maria'],
]

for indice, valor in lista:
    print(indice, valor)
