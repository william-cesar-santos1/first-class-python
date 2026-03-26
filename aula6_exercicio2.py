'''
Dado a lista de produtos abaixo. Reajuste o preço de venda de todos em 10%.
Compreensão de dicionários para criar um novo dicionário com os preços reajustados.
'''
produtos = [
    {'nome': 'Notebook', 'preco': 2500.00},
    {'nome': 'Monitor', 'preco': 800.00},
    {'nome': 'Teclado', 'preco': 150.00},
    {'nome': 'Mouse', 'preco': 100.00}
]

# Desempacotamento de dicionários usando compreensão 
# de dicionários para criar um novo
# ** desempacota o dicionário original, permitindo acessar suas chaves diretamente
# * desempacota das chaves do dicionário para criar um novo dicionário com 
# as mesmas chaves e valores
# Round faz um arredondamento do valor para 2 casas decimais
produtos_com_preco_reajustado = [ 
                                 {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
                                 for produto in produtos 
                                ]
print(produtos_com_preco_reajustado)