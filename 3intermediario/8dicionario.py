
d1 = {'chave1':'valor da chave'}
print(d1)
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
print(d1['chave1'])

d2=dict(chave1='Valor da chave', chave2='Valor da outra chave')
d2['nova_chave'] = 'Valor da nova chave'
print(d2)
print(d2['chave2'])

d3 = {1:'valor', 2:'valor', 2: 'valor da real chave'}
print(d3[2])