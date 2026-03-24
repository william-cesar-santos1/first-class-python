'''
iteraveis(iterable) = listas, tuplas, dicionários, conjuntos, strings
for item in iteravel:

iteradores(iterator) = objetos que permitem percorrer os elementos de um 
  iterável, um por um, sem a necessidade de acessar os índices diretamente. 
  Eles mantêm um estado interno que rastreia a posição atual durante a iteração.
iterador = iter(iteravel)
next(iterador)

iterator = iter(iteravel)
while(hasNext(iterador)):
    variavel = next(iterador)
'''
numeros = [1, 2, 3, 4, 5]
iterador = iter(numeros)
print(next(iterador))  # Imprime 1
print(next(iterador))  # Imprime 2
print(next(iterador))  # Imprime 3
print(next(iterador))  # Imprime 4
print(next(iterador))  # Imprime 5
print(next(iterador))  # Error: StopIteration, pois não há mais elementos para iterar