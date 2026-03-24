'''
Dado o dicionário abaixo, com o nome e ano de nascimento de algumas pessoas, 
  calcule a idade de cada pessoa e inclua essa informação no dicionário.
Inserção de nova chave e valor em um dicionário:
dicionario[chave_nova] = valor_novo
'''
pessoas = {
    'Alice': {
        'ano_nascimento': 1990
    },
    'Bob': {
        'ano_nascimento': 1985
    },
    'Charlie': {
        'ano_nascimento': 2000
    }
}

# Adição de uma nova chave 'idade' para cada pessoa, calculando a idade 
# com base no ano de nascimento
pessoas['Alice']['idade'] = 20