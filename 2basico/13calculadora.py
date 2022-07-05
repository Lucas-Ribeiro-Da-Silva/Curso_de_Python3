#faça uma calculadora básica com os conceitos aprendidos até ent

while True:
    num1 = input('Digite um número:')
    op = input('Digite o operador:')
    num2 = input('Digite outro número:')
    sair = input('Deseja sair? [s]im [n]ão')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('você precisa digitar um número')
        continue

    num1 = int(num1)
    num2 = int(num2)

    # + - * / **
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == "**":
        print(num1**num2)
    else:
        print('operador inválido')