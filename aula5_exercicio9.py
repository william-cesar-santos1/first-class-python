'''
Agrupe os produtos por categoria.
    - Categoria: Eletrônicos, [Notebook, Monitor]
    - Categoria: Periféricos, [Teclado, Mouse]
    ...
'''
produtos = [
    {'categoria': 'Eletrônicos', 'nome': 'Notebook'},
    {'categoria': 'Periféricos', 'nome': 'Mouse'},
    {'categoria': 'Periféricos', 'nome': 'Teclado'},
    {'categoria': 'Eletrônicos', 'nome': 'Monitor'},
    {'categoria': 'Alimento', 'nome': 'Arroz'},
    {'categoria': 'Veículos', 'nome': 'HB20'},
    {'categoria': 'Alimento', 'nome': 'Feijão'},
    {'categoria': 'Veículos', 'nome': 'Gol'},
    {'categoria': 'Alimento', 'nome': 'Macarrão'}
]
produtos_agrupados = {}
for produto in produtos:
    categoria = produto['categoria']
    if categoria not in produtos_agrupados:
        produtos_agrupados[categoria] = []
    produtos_agrupados[categoria].append(produto['nome'])
print(produtos_agrupados)