"""
função range(start=0, stop, step=1)
o valor de stop não é incluido
"""


texto = 'python'
##########################
print(20*'#')
for letra in texto:
    print(letra)
###################################################################################
print(20*'#')
for n, letra in enumerate(texto): #a função enumarate enumara a cada volta do laço
    print(n, letra)
###################################################################################
print(20*'#')
for n in range(20, 10, -1):
    print(n)
######################################################
print(20*'#')
for n in range(0, 100, 8): #achar multiplos de 8
    print(n)
print(20*'#')
######################################################
texto ='Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra =='h':
        nova_string += letra.upper()
        break
    else:
        nova_string+=letra
print(nova_string)