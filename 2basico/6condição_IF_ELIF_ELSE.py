"""
condições if eelif else

atenção para a identação

len: função usada para contar caracteres de strings
"""

#cadastro do usuario e senha
user = input('criar usuário:')
pin = input('criar senha(6 ou mais caracteres):')
qtd = len(pin)

if qtd>=6:
    usuario = user
    senha = pin
    print('usuário e senha cadastrados!')
else:
    print('atenção, a senha deve conter 6 ou mais caracteres!')
    user = input('criar usuário:')
    pin = input('criar senha(6 ou mais caracteres):')
    qtd = len(pin)

    if qtd >= 6:
        usuario = user
        senha = pin
        print('usuário e senha cadastrados!')
    else:
        print('muitas tentaivas, usuário bloqueado')
#acessar o sistema
acesso_user = input('usuário:')
acesso_pin = input('senha:')

if acesso_user in usuario and acesso_pin==senha:
    print('você acessou o sistema!')
else:
    print('usuário ou senha incorretos!')
    acesso_user = input('usuário:')
    acesso_pin = input('senha:')

    if acesso_user == usuario and acesso_pin == senha:
        print('você acessou o sistema!')
    else:
        print('muitas tentaivas, usuário bloqueado')