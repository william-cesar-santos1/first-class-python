'''
Função reduce() é uma função embutida em Python que permite aplicar uma função 
  de redução a um iterável (como uma lista) para reduzir os elementos a 
  um único valor. A função reduce() é útil para realizar operações acumulativas, 
  como somar, multiplicar ou concatenar elementos de forma eficiente.
'''
from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = lambda numero_um, numero_dois: numero_um + numero_dois
resultado = reduce(soma, numeros)
print(resultado)

nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo']
concatenar = lambda nome_um, nome_dois: nome_um + '-|-' + nome_dois
resultado_nomes = reduce(concatenar, nomes)
print(resultado_nomes)