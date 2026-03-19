'''
Peça ao usuário que informe o próprio nome.
Conte quantas vogais existem no nome informado.
Exemplo: Se o usuário informar o nome "William", o resultado deve ser:
O nome "William" possui 3 vogais.

Precisa utilizar for para resolver.
for letra in nome:
'''
nome = input('Digite seu nome: ')
contador_vogais = 0
for letra in nome:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']: #'aeiou'
        contador_vogais += 1
print(f'O nome "{nome}" possui {contador_vogais} vogais.')