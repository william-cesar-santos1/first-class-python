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

tabuada = [f'{numero_um} x {numero_dois} = {numero_um * numero_dois}' 
           for numero_um in range(1, 11) 
           for numero_dois in range(1, 11)]

for linha in tabuada:
    print(linha)