"""
Faça um programa que peça ao usuário para digitar um número inteiro
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('digite um numero inteiro: ')
if num.isdigit():
    num = int(num)
    par=num%2
    if par==0:
        print('é par')
    else:
        print('é impar')
else:
    print('não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('que horas são?(0-23)')
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('o horario deve estar escrito entre 0 e 23')
    else:
        if hora <=11:
            print('Bom dia')
        elif hora <=17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('o horario deve estar escrito entre 0 e 23')


"""
Faça um programa que peça o primeiro nome do usuário . Se o nome tiver 
4 letras ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras , escreva
"seu nome é normal"; maior que 6 escreva "Seu nome é grande"
"""
nome = input('seu nome é? ')
qtd = len(nome)

if qtd <=4:
    print('seu nome é curto')
elif qtd <=6:
    print('seu nome é normal')
else:
    print('seu nomeé muito grande')
