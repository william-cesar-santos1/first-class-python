'''
Dado a lista de palavras = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
Crie uma nova lista com a quantidade de letras que cada palavra possui, 
  utilizando compreensão de listas.
Para descobrir quantas letras uma palavra possui, utilize a função len() do Python.
len == length (comprimento)
'''
palavras = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
quantidade_letras = [len(palavra) for palavra in palavras]
print(quantidade_letras)