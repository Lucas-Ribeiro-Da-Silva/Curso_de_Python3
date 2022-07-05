'''
Criar váriaveis para nome (str), idade(int),altura (float), peso(float) de uma pessoa
Criar váriavel com o ano atual (int)
obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
usar inputs
'''

nome = input('nome?')
idade = int(input('idade?'))
altura = float(input('altura?'))
peso = float(input('peso?'))
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} Kg.\n'
      f'O IMC de {nome} é {imc:.2f}.\n{nome} nasceu em {ano_nasc}')