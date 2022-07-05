variavel =['LUiz Otavio', 'Joaozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'): #startswith checa se começa com tal coisa, lower transforma em minuscula
        print('começa com j')
    else:
        print('não começa com j')


variavel =['LUiz Otavio', 'Joaozinho', 'Maria']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('existe uma palavra aque começa com j')
else:
    print('nao existe uma palavra que começa com j')
