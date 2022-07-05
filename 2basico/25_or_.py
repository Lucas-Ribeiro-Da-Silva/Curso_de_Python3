nome = input('Qual  seu nome?')

if nome:
    print(nome)
else:
    print('Voce não digitou nada = !')

#agora usando or

nome = input('Qual  seu nome?')
print(nome or 'Você não digitou nada!')

#dnv

nome = input('Qual  seu nome?')
print(nome or None or False or 0 or 'Você não digitou nada!')

#outra

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g #recebe o primeiro True que encontrar

print(variavel)

