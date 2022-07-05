logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

#ou..................

logged_user = False

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'

print(msg)

#exemplo.....................

idade = 18
if idade>=18:
    print('Pode acesar.')
else:
    print('Não pode acessar')

#ou................

idade = input('Qual a sua idade?')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade>=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg)
