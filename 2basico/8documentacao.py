"""
link: https://docs.python.org/3/library/stdtypes.html
tipos de funções built-in, ou seja, são funções que ja vem de fábrica com o python
"""
#este código de exemplo fornece um erro se não for adicionado um número a ele
num1 = input('Digite um número:')
num2 = input('Digite um número:')
num1 = int(num1)
num2 = int(num2)
print(num1+num2)

#funções built-in podem solucionar esse problema, como exemplo:
#isdigit, isnumeric, isdecimal
#conferem se o valor é um numero inteiro positivo apenas
num1 = input('Digite um número:')
num2 = input('Digite um número:')
if num1.isdigit() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('não foi possível converter o valor inserido')

#o código a seguir é de conteúdo avançado, solução para o problema atual mas que ainda será ensinado

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False

num1 = input('Digite um número:')
num2 = input('Digite um número:')
if num1.is_number() and num2.is_number():
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
else:
    print('error')

#a ultima solução é usar a função try except
#ela tenta executar algo e a qualquer erro ela nao exibe a mensagem de erro
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
except:
    print('error')