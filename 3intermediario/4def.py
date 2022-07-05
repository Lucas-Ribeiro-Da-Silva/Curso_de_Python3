#uma variavel global que é alterada dentro de um def deve ser definida com a função "global"
#se isso não for feito ela será como uma otra variavel apesar do mesmo nome

variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'
    print(variavel)

func2()
print(variavel)

def func3():
    global variavel
    variavel = 'Outro valor'
    print(variavel)

func()
func3()
print(variavel)

