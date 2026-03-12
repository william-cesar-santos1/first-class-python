'''
Peça ao usuário a idade de uma pessoa e imprima 
  se é maior de idade ou não.
  Exemplo: [nome] é maior de idade: True
'''
nome = input('Informe o nome da pessoa: ')
idade = input('Informe a idade da pessoa: ')
maior_idade = int(idade) >= 18
print(f'{nome} é maior de idade: {maior_idade}')