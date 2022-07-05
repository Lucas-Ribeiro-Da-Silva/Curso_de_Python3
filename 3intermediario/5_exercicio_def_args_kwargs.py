"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def ola_mundo():
     return 'Olá mundo!'

def mestre(funcao):
     return funcao()

executando = mestre(ola_mundo)
print(executando)
print(ola_mundo())

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""


def mestre1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre1(fala_oi, 'Luiz')
executando2 = mestre1(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
