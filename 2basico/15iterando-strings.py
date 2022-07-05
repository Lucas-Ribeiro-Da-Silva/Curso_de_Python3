#se o elemento tem indices ele é iteravel

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

#iteração
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)

#########################################################################

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

#########################################################################

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
while contador < tamanho_frase:
    nova_string += frase[contador]
    contador += 1
    print(nova_string)
print(40*'#')
print(nova_string)