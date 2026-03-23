'''
Dado a lista de nomes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
Crie uma nova lista contendo apenas os nomes que contenhas a letra 'a' 
  ou 'A' e aplique uma transformação para deixar os nomes em maiúsculo.
'''
nomes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
nomes_com_a = [nome.upper() for nome in nomes if 'a' in nome.lower()]
print(f'Resultado: {nomes_com_a}')