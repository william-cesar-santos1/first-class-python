'''
Crie um função pura que receba duas lista de números. Retorne apenas a interseção 
  entre as duas listas, ou seja, os números que estão presentes em ambas as listas.
'''
lista_um = [1, 2, 3, 4, 5]
lista_dois = [4, 5, 6, 7, 8]
def intersecao(lista_um, lista_dois):
    return [numero for numero in lista_um if numero in lista_dois]
  
print(intersecao(lista_um, lista_dois))