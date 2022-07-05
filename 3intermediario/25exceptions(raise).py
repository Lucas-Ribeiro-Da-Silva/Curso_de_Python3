#https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Log: ',error)
        raise

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)

#sem o raise o segundo try não executa

def divide1(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print( error)
        return False

try:
    print(divide1(2, 0))
except:
    print('erro')



#criando meu próprio erro

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

print(divide2(2, 1))
print(divide2(2, 0))