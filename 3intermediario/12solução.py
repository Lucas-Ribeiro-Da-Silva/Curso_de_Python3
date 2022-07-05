"""
usando list comprehension fazer:
string = '0123456789012345678901234567890123456789'
lista = ['0123456789', '0123456789', 0123456789', '0123456789']
retorno = '0123456789.0123456789.0123456789.0123456789'
"""
"""
#eu poderia iterar cada item da lista com list comprehension
string = '0123456789012345678901234567890123456789'
comp = [letra for letra in string]
print(comp)

#eu poderia exibir um determinado numero de iteraveis da lista e replicar
print(string[0:10])
print(string[10:20])
print(string[20:30])
print(string[30:40])

#separa tuplas indicando onde começa e termina as repetições
n = 10
comp1 = [(i, i+n) for i in range(0, len(string), n)]
print(comp1)

#fazer o fatiamento
n = 10
comp2 = [(i:i, i+n) for i in range(0, len(string), n)]
print(comp2)
"""

#por fim, unir os grupos fatiados com pontos
string = '0123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(retorno)

"""
#exemplo de aplicação
string = '0123456789012345678901234567890123456789'
n = 10
contadres = [i for i in range(0, len(string), n)]
tuplas = [i,i + n] for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}:{i+ n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(contadores)
print(tuplas)
print(raw)
print(lista)
print(retorno)
"""