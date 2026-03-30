'''
Dado uma lista de nomes. Conte quantas vezes cada nome aparece na lista 
  e imprima o resultado.
Exemplo de entrada:
nomes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
Saída esperada:
Alice: 3
Bob: 2
Charlie: 1

Utilize uma função para realizar essa contagem e retorne um dicionário 
  onde as chaves são os nomes e os valores são as contagens correspondentes.
'''

def contar_nomes(nomes):
    return {nome: nomes.count(nome) for nome in nomes}
  
nomes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
resultado = contar_nomes(nomes)
print(resultado)