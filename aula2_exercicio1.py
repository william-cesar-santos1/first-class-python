'''
Crie uma interação com o usuário para capturar os dados de entrada (input).
Peça ao usuário qual o seu nome e idade, e imprima uma mensagem:
Bem vindo, [nome do usuário]! Espero que os seus [idade do usuário] 
  anos tenham sido repletos de saúde, paz e prosperidade!
'''
nome = input('Informe o seu nome: ')
print(type(nome))
idade = int(input('Informe a sua idade: '))
print(type(idade))
print(f'Bem vindo, {nome}! Espero que os seus {idade} anos tenham sido repletos de saúde, paz e prosperidade!')