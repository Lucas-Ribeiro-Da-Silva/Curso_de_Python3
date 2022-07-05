'''
Tipos de dados
str - string - textos 'Assim' ou "Assim"
int - inteiro - 123456789 0 -10 -500
float - real/ponto flutuante - 10.5 11.3 -10.7 0.0
bool - booleano/lógico - True/False 10==10 11!=9

a função "type" retorna a classe do dado
fazer um "type cast" significa mudar a classe de uma variavel
'''

print('Lucas', type('Lucas'))
print('10', type('10'))
print(10, type(10))
print(10.10, type(10.10))
print('l'=='L', type('l'=='L'))

n= 10
print(n, type(n), bool(n), type(bool(n)))
