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

for chave, valor in dicionario.items():
    print(f'{chave=},{valor=}')

for chave in dicionario:
    print(f'{chave=}')
    print(f'{dicionario[chave]=}')