'''
Utilizando do conceiro de clousure(funções aninhadas), crie uma função 
  que seja um aplicador de desconto ao preço de um produto. 
A função externa deve receber o valor do desconto em percentual e retornar 
  uma função interna que, por sua vez, deve receber o preço do produto e 
  retornar o preço com o desconto aplicado.
'''

def aplicador_de_desconto(desconto):
    def aplicar(preco):
        return preco * (1 - desconto / 100)
    return aplicar

desconto_10 = aplicador_de_desconto(10)
print(desconto_10(100))  # Saída: 90.0
desconto_20 = aplicador_de_desconto(20)
print(desconto_20(100))  # Saída: 80.0