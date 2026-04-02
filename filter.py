'''
Função filter() é uma função embutida em Python que permite filtrar 
  elementos de um iterável (como uma lista) com base em uma condição. 
  A função filter() retorna um novo iterável contendo apenas os elementos 
  que satisfazem a condição. A função filter() é útil para 
  selecionar ou excluir elementos de forma eficiente.
'''
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gustavo']
nomes_com_a = lambda nome: 'a' in nome.lower()
nomes_filtrados = filter(nomes_com_a, nomes)
print(list(nomes_filtrados))