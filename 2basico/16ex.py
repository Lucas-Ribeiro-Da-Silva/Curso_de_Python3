#método ruim
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = 0
for produto in carrinho:
    total += produto[1]
print(total)

#pequena melhoria
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))

#jeito correto
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)
#mesma coisa que: produto, preco = carrinho[0]

