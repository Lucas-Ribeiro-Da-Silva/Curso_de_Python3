"""
sep = "" usado para indicar o separador dos argumentos em print
end = "" usado para indicar como um print deve ser encerrado
r'        usado para ignorar todos os comandos que são executaveis dentro de um print
\n       usado para continuar a instrução na linha de baixo
\n\n     usado para pular uma linha
\        usado para ignorar o comando executado a seguir
para  formatar prints usamos f', .format ou %

:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(NÙMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

>-Esquerda
<-Direita
^-Centro
"""

nome = "Lucas"
altura = 18.75

print('usando "aspas" assim')
print('usando \'aspas\' assim')
print(r'usando r para ignorar comandos como \n')
print('sem o r a linha seria pulada assim \n por isso usamos o r')

print('')

print(nome, 'e', altura, sep='-')

print(nome, end='=')
print(altura)
print('')

print('olá', nome, 'você tem', altura, 'de altura')
print('olá', nome, 'você tem %.1f de altura' % altura)

print(f'olá {nome} você tem {altura} de altura')
print(f'olá {nome} você tem {altura:.1f} de altura')

print('olá {} você tem {} de altura'.format(nome, altura))
print('olá {} você tem {:.1f} de altura'.format(nome, altura))
print('olá {0} você tem {1:.1f} de altura {1} {0}'.format(nome, altura))
print('olá {n} você tem {a:.1f} de altura'.format(n=nome, a=altura))

print('olá'
      'lucas')


################### formatando valores #########################

n = 18
name = 'lUcAs'

print(f'{n:0<10}') #adiciona zeros a direita do valor
print(f'{n:0>10}') #adiciona zeros a esquerda do valor
print(f'{n:0^10}') #centraliza o valor no meio dos zeros
print(f'{n:.10f}') #como float indica 10 casas decimais ao numero
print(f'{n:d}') #como int indica neenhuma casa decimal
print(f'{name:s}') #como str indica texto

print(f'{name:0^10}')
print(f'{name:0>10}')
print(f'{name:0<10}')

print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #primeiras letras maiusculas
#print(nome."digite a função desejada"())

