'''
Função map() é uma função embutida em Python que permite aplicar uma 
  função a cada item de um iterável (como uma lista) e retornar um novo 
  iterável com os resultados. A função map() é útil para transformar ou 
  processar dados de forma eficiente.
'''
numeros = [1, 2, 3, 4, 5]
quadrado = lambda numero: numero ** 2
numeros_quadrados = map(quadrado, numeros)
print(list(numeros_quadrados))