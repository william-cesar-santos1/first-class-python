'''
Dado a lista de cliente abaixo. Crie uma função lambda para 
  filtrar apenas os clientes com rating A e AA.
'''
clientes = [
    {
        'name': 'Alice',
        'rating': 'AA',
    },
    {
        'name': 'Bob',
        'rating': 'A',
    },
    {
        'name': 'Charlie',
        'rating': 'B',
    }
]
filtrar_rating = lambda cliente: cliente['rating'] in ['A', 'AA']
clientes_filtrados = filter(filtrar_rating, clientes)
print(list(clientes_filtrados))