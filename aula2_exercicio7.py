'''
Peça ao usuário que informe o valor do produto 
  e o percentual de desconto. 
Imprima o valor do desconto e o valor final do produto.
'''
preco = float(input('Informe o valor do produto: '))
desconto = float(input('Informe o percentual de desconto: '))
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
print(f'O valor do desconto é: {valor_desconto:.2f}')
print(f'O valor final do produto é: {preco_final:.2f}')