'''
nome da função deve ser um verbo ou uma expressão verbal que 
  descreva claramente a ação que a função realiza. Sem caracteres especiais, 
  acentos ou espaços. Use letras minúsculas e, se necessário, separe as palavras 
  com underline (_).
  
def nome_funcao(parametros):
    conteudo da função
    return valor_de_retorno
'''

# Declaração de uma função simples que imprime "Olá, mundo!"
def ola_pessoa(nome):
    print(f"Olá, {nome}!")

def soma(a, b):
    resultado = a + b
    ola_pessoa(resultado)
    return resultado

def max_min(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    return minimo, maximo

# Chamada da função para executar seu código
print(max_min([3, 1, 4, 7, 5, 9]))  # Exemplo de uso da função max_min