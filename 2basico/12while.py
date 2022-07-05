"""
while é utilizado para realizar ações enquanto uma condição for verdadeira
"""

x = 0
while x<100:
    print(x)
    x += 1
print('agr está verdadeira, ent o laço encerrou')

print(15*'#')

x = 0
while x < 10:
    if x == 3:
        x += 1
        continue
        #a exprressão continue faz com que as expressões abaixo nao sejam executadas e a instrução volte para o inicio do laço
    print(x)
    x += 1

print(15*'#')

x = 0
while x < 10:
    if x == 3:
        x += 1
        break
        #a exprressão break faz com que o laço seja interrompido
    print(x)
    x += 1

print(15*'#')

#é possivel tmb fazer loops dentro de loops
x=0 #coluna
while x<10:
    y=0 # linha

    while y<5:
        print(f'({x},{y})')
        y+=1

    x+=1
    
print('acabou')

print(15*'#')

while True: # loop infinito
    nome = input("Qual o seu nome?")
    print(f'Olá {nome}!')
print('Não será executada pois while nunca é falso')
