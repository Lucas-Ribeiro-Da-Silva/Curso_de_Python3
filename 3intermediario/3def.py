"""
Funções def em python - *args **kwargs
"""
#argumentos obrigatórios sempre vem antes dos opcionais, senão dá erro.
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)

##################################################

def func2(*args): #não sei quantos argumentos devem existr
    print(args)

#desempacotando listas
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)

#desempacotando listas
lista = [1, 2, 3, 4, 5]
print(*lista, sep=',')

#armazena em uma tupla
func2(1, 2, 3, 4, 5)

#OBS: uma tupla não pode ter nenhum de seus valores alterados
#mas ela pode ser covertida em uma lista

def func3(*args): #não sei quantos argumentos devem existr
    args = list(args)
    args[0] = 20
    print(args)

func3(1, 2, 3, 4, 5)


#nas tuplas podemos separar argumentos que tenham keyword
def func4 (*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    if nome is not None:
        print(nome)
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func4(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

