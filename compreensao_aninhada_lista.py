nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
sobrenomes = ['Silva', 'Oliveira']

combinacoes = [f'{nome} {sobrenome}' for nome in nomes for sobrenome in sobrenomes]
print(combinacoes)
'''
for nome in nomes:
    for sobrenome in sobrenomes:
        combinacao = f'{nome} {sobrenome}'
        print(combinacao)
'''