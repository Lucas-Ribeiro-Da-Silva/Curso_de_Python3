"""
usando list comprehension fazer:
string = '0123456789012345678901234567890123456789'
lista = ['0123456789', '0123456789', 0123456789', '0123456789']
retorno = '0123456789.0123456789.0123456789.0123456789'
"""

#usando for
string = '0123456789012345678901234567890123456789'
variavel = ''
confere = ''
for x in string:
    if x in confere:
        variavel += '.'
        confere = ''
    variavel += x
    confere += x
print(variavel)