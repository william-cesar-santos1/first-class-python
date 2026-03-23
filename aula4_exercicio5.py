'''
Você deve criar um programa que analise dados de vendas de uma loja.

Entrada

O programa deve trabalhar com uma lista de vendas no seguinte formato:
vendas = [
    ["Notebook", 3500, 2],
    ["Mouse", 80, 10],
    ["Teclado", 150, 5],
    ["Monitor", 900, 3],
    ["Mouse", 80, 2],
    ["Notebook", 3500, 1]
]

Cada item da lista representa:
[nome_do_produto, preço_unitário, quantidade_vendida]


Desafios
 - Faturamento total. Calcule o faturamento total da loja.
 - Ticket médio. Calcule o ticket médio total.
 - Pedido mais caro.
'''
vendas = [
    ["Mouse", 80, 10],
    ["Teclado", 150, 5],
    ["Notebook", 3500, 2],
    ["Monitor", 900, 3],
    ["Mouse", 80, 2],
    ["Notebook", 3500, 1]
]

faturamento_total = 0
pedido_mais_caro = vendas[0]

for venda in vendas:
    nome_produto = venda[0]       # nome do produto vendido
    preco_unitario = venda[1]     # preço unitário do produto
    quantidade_vendida = venda[2] # quantidade vendida
    valor_total_venda = preco_unitario * quantidade_vendida  # valor total da venda

    faturamento_total += valor_total_venda

    # Aqui multiplica novamente o preço unitário pela quantidade vendida para comparar o valor total da venda com o valor do pedido mais caro
    valor_pedido_mais_caro = pedido_mais_caro[1] * pedido_mais_caro[2]
    if valor_total_venda > valor_pedido_mais_caro:
        print('Novo pedido mais caro encontrado:', nome_produto, '- R$', valor_total_venda)
        pedido_mais_caro = venda

ticket_medio = faturamento_total / len(vendas)

print('Faturamento total: R$', faturamento_total)
print('Ticket médio: R$', ticket_medio)
print('Pedido mais caro:', pedido_mais_caro[0], '- R$', pedido_mais_caro[1] * pedido_mais_caro[2])