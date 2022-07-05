"""
jogo da advinhação
"""

secreto = 'perfume'
digitadas = [] #lista vazia
chances = 5

while True:
    if chances <= 0:
        print('você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra)>1:
        print('isso não vale kkkk digite somente uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'boa lek, a letra {letra} existe na palavra secreta')
    else:
        print(f'putz que pena, a letra {letra} não existe na palavara secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario  += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, você ganhou!!!, a palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'a palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -=1
    print(f'você ainda tem {chances} chances.')
    print('')
