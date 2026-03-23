# comprehension de listas
# A compreensão de listas é uma forma concisa de criar listas em Python. 
# Ela permite criar uma nova lista a partir de uma sequência existente, 
# aplicando uma expressão a cada elemento da sequência. A sintaxe básica é:
# nova_lista = [expressão for item in sequência if condição]
# A expressão é avaliada para cada item na sequência, e o resultado é 
# adicionado à nova lista se a condição for verdadeira. 
# A compreensão de listas é uma maneira eficiente e legível de criar listas em Python.

numeros = [1, 5, 8, 6, 15, 20, 34, 30, 20, 19, 11]
'''
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
'''
pares = [numero * 2 for numero in numeros if numero % 2 == 0]

print(pares)