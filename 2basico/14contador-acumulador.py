contador = 1
acumulador = 1
while contador<=10:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else: #quando o while virar falso ele executa o else
    print('cheguei no else')
print('acabou')

#se ocorrer um break o else não executa
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    if contador>5:
        break
    acumulador += contador
    contador += 1
else:  # quando o while virar falso ele executa o else
    print('cheguei no else')
print('acabou')