'''
Dado uma quantidade indefinida de números, crie uma função capaz de 
  identificar o maior número par e o menor número impar.
A função deve retornar ambos os números encontrados.
'''
numeros = [3, 1, 4, 7, 5, 9, 2, 8, 6]

def par(numero):
    return numero % 2 == 0
  
def maior_par_menor_impar():
    maior_par = None
    menor_impar = None
    
    for numero in numeros:
        if par(numero):
            if maior_par is None or numero > maior_par:
                maior_par = numero
        else:
            if menor_impar is None or numero < menor_impar:
                menor_impar = numero
                
    return maior_par, menor_impar

maior_par, menor_impar = maior_par_menor_impar()
print(f'Maior número par: {maior_par}')
print(f'Menor número ímpar: {menor_impar}')