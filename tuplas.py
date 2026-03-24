'''
Tuplas são estruturas de dados semelhantes às listas, mas são imutáveis. 
  Isso significa que, uma vez criada uma tupla, seus elementos não podem ser 
  alterados. 
As tuplas são definidas usando parênteses () e os elementos são 
  separados por vírgulas.
'''
tupla_numeros = (1, 2, 3, 4, 5) # tupla - não posso alterar
for numero in tupla_numeros:
    print(numero, end=', ')
print()
tupla_nomes = tuple(['Alice', 'Bob', 'Charlie']) # tupla - não posso alterar    
for nome in tupla_nomes:
    print(nome, end=', ')
print()
'''
Desempacotamento de tuplas(unpacking)
O desempacotamento de tuplas é um recurso que permite atribuir os elementos 
  de uma tupla a variáveis individuais de forma concisa. 
  Ele é útil quando você deseja extrair valores específicos de uma tupla 
  sem precisar acessar cada elemento individualmente.
'''
primeiro, segundo, *_ = tupla_numeros
print(f"Primeiro: {primeiro}, Segundo: {segundo}, Resto: {_}")

primeiro, *_, ultimo = tupla_numeros
print(f"Primeiro: {primeiro}, Último: {ultimo}, Resto: {_}")

*_, penultimo, ultimo = tupla_numeros
print(f"Penúltimo: {penultimo}, Último: {ultimo}, Resto: {_}")

tupla_juntado_tudo = tupla_numeros + tupla_nomes
print(f'{tupla_juntado_tudo=}')

# Tupla implicita
numero_um, numero_dois = 1, 2

# Uso de tupla em loop
numeros = list(range(1, 11))
for index, numero in enumerate(numeros): # (0-indice,1),(1,2),(2,3),(3,4),...
    if numero % 2 == 0:
        numeros[index] = numero ** 2
    else:
        numeros[index] = numero ** 3
print(sorted(numeros))