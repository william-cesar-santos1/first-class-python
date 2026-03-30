'''
Palavra é um palíndromo se ela for lida da esquerda para a direita 
  ou da direita para a esquerda, ela tem a mesma sequência de caracteres.
Por exemplo, "arara" é um palíndromo, pois é lida da mesma forma em 
  ambas as direções. Já "banana" não é um palíndromo, pois a sequência 
  de caracteres difere quando lida de trás para frente.
  
Crie uma função que receba uma palavra como parâmetro e retorne
  True se a palavra for um palíndromo e False caso contrário.
'''

def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]
  
print(f'arara é palíndromo? {eh_palindromo("arara")}')  # True
print(f'banana é palíndromo? {eh_palindromo("banana")}')  # False