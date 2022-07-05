"""
Funções def em python
"""

def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3') #replace substitui um valor por outro
    print(msg, nome)

saudacao(nome='Zezinho', msg='Hi')
saudacao('oi', 'luiz')

def funcao_sem_argumento():
    print('esta função não precisa de argumento')

funcao_sem_argumento()

"""
parte 2: print exibe, return retorna.
"""

#o print exibe um valor mas não o armazena, por isso aqui o valor retornado é None(Falso)
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')
print(variavel)

if variavel:
    print(variavel)
else:
    print('nenhum valor')

#para retornar um valor que possa ser atribuido a variavel usamos o return
def funcao1(var):
    return var

variavel = funcao1('Valor que eu quero')
print(variavel)

if variavel:
    print(variavel)
else:
    print('nenhum valor')


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1/n2
divide = divisao(8,0)

if divide:
    print(divide)
else:
    print('Conta inválida')


divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta inválida')

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('blaaaaaa')