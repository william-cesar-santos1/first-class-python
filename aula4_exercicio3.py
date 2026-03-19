'''
Peça ao usuário que informe um número. Gere uma lista com os números 
  de 1 até o número informado.(range)
Percorra com um for a lista e aplique potencia de 2 para os 
  números pares, e potencia de 3 para os números ímpares.(for com enumerate)
Substitua os números da lista pelos resultados das potências. lista[index]
Imprima o resultado de forma ordenada. sorted

Exemplo: Se o usuário informar o número 5, o resultado deve ser:
1**3 = 1
2**2 = 4
3**3 = 27
4**2 = 16
5**3 = 125

Resultado:
[1, 4, 16, 27, 125]
'''
limite = int(input('Digite um número: '))
numeros = list(range(1, limite + 1))
for index, numero in enumerate(numeros):
    if numero % 2 == 0:
        numeros[index] = numero ** 2
    else:
        numeros[index] = numero ** 3
print(sorted(numeros))