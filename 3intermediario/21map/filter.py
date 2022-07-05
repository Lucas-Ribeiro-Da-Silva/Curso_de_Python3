from dados import produtos, pessoas, lista

nova_lista0 = filter(lambda x: x>5, lista)
#nova_lista0 = [x for x in lista if x>5]
print(nova_lista0)



def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False
nova_lista = filter(filtra, pessoas)
for person in nova_lista:
    print(person)





def filtra1(produto):
    if produto['preco'] > 50:
        produto['é_caro'] = True
    return True

nova_lista1 = filter(filtra1, produtos)

for produto in nova_lista1:
    print(produto)
