'''
Dado a lista de números abaixo. Crie uma função lambda para ordenar a lista 
  em ordem crescente.
'''
numeros = [5, 2, 9, 1, 5, 6]
ordenados = sorted(numeros, key=lambda x: x)
print(ordenados)