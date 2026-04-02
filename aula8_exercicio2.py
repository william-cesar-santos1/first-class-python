'''
Dado a lista de nomes abaixo, crie uma função pura que retorne apenas os nomes 
  que contenham mais de 5 letras.
'''
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gustavo']
def nomes_com_mais_de_5_letras(nomes):
    return [nome for nome in nomes if len(nome) > 5]
  
print(nomes_com_mais_de_5_letras(nomes))