"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def funcao(saud="saudação", nome='nome'):
    print(saud, nome)

funcao('oi', 'lucas')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(n1, n2, n3):
    print("n1+n2+n3=%d" % (n1+n2+n3))
soma(1,1,1)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def percent(n1, n2):
    n1 += n1*(n2/100)
    return n1
variavel = percent(1,100)
print(variavel)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def FizzBuzz(var):
    if var%3 == 0 and var%5 == 0:
        return "FizzBuzz"
    if var % 3 == 0:
        return "Fizz"
    if var % 5 == 0:
        return "Buzz"
    return var

print(FizzBuzz(15))
print(FizzBuzz(9))
print(FizzBuzz(10))
print(FizzBuzz(8))