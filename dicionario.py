'''
Dicionarios são estruturas de dados que armazenam pares de chave-valor. 
  Eles são mutáveis, o que significa que podem ser alterados após a criação. 
  As chaves em um dicionário devem ser únicas e imutáveis (como strings, 
  números ou tuplas), enquanto os valores podem ser de qualquer tipo.
Os dicionários são definidos usando chaves {} e os pares de chave-valor são 
  separados por vírgulas. A sintaxe básica para criar um dicionário é:
dicionario = {
    'chave1': valor1,
    'chave2': valor2,
    ...
}
Você pode acessar os valores em um dicionário usando as chaves correspondentes. 
  Por exemplo:
  valor = dicionario['chave1']
Além disso, os dicionários possuem métodos úteis para manipulação, 
  como adicionar, remover ou atualizar elementos.
'''

dicionario = {
    'nome': 'William César dos Santos',
    'idade': 36,
    'salario': 1545.15,
    'estudante': False,
    'hobbies': ['programação', 'futebol', 'música']
}

# Acesso a valores do dicionário usando chaves
print(dicionario['nome'])  # Acessa o valor associado à chave 'nome'
print(dicionario['idade'])  # Acessa o valor associado à chave 'idade'
# Acesso seguro usando o método get, que retorna None ou um valor padrão se a chave não existir
print(dicionario.get('data_nascimento', '2020-01-01'))

# Adicionando um novo par chave-valor ao dicionário
dicionario['data_nascimento'] = '2000-01-01'
print(dicionario['data_nascimento'])

# Percorrer por chave e valor usando items()
for chave, valor in dicionario.items():
    print(f'{chave=},{valor=}')

# Percorrer por chave
for chave in dicionario:
    print(f'{chave=}')
    print(f'{dicionario[chave]=}')

# Removendo um par chave-valor do dicionário usando del
print('Removendo a chave "estudante" usando del')
del dicionario['estudante']
print(dicionario)

print('Removendo a chave "salario" usando pop')
dicionario.pop('salario')  # Remove o par chave-valor associado à chave 'salario'
print(dicionario)

# dicionario.keys() retorna uma visão das chaves do dicionário
print(dicionario.keys())

# dicionario.values() retorna uma visão dos valores do dicionário
print(dicionario.values())

print('Criando um novo dicionário com chaves em maiúsculas usando compreensão de dicionários')
novo_dicionario = { chave.upper() : valor for chave, valor in dicionario.items()}
print(novo_dicionario)