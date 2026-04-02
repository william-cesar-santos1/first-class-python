'''
Crie um função pura que receba a lista de número abaixo e retorne 
  apenas o número pares.
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def pares(numeros):
    return [numero for numero in numeros if numero % 2 == 0]
  
print(pares(numeros))