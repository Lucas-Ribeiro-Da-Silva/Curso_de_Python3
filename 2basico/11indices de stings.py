"""
Manipulando stings
strings indice
fatiamento de strings [inicio:fim:passo]
funções built-in len, abs, type, print, etc...
essas funções podem ser usadas diretamente em cada tipo

https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
"""

#positivos: [0123456789]
nome = '0123456789'
print(nome[9])

#negativos [...-9-8-7-6-5-4-3-2-1]
print(nome[-1])

print(nome[2:6])  #o fim não é incluido

print(nome[0:9:2]) #0 ou vazio da na mesma

#exemplo de aplicação
site = 'www.google.com/'
print(site[:14])