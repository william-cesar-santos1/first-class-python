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

# quantidade indefinida de parâmetros. O Python trata isso usando *args para parâmetros posicionais
def media_simples(*numeros):
    return sum(numeros) / len(numeros)

resultado_media_simples = media_simples(10, 20, 30)
print(f'Média simples: {resultado_media_simples}')

#resultado_media_simples = media_simples([5, 15]) # Isso não funcionará porque a função espera números individuais, não uma lista
resultado_media_simples = media_simples(*[5,15]) # Usando * para desempacotar a lista em argumentos individuais
print(f'Média simples: {resultado_media_simples}')


def cadastro(nome, idade, email):
    return f'Nome: {nome}, Idade: {idade}, Email: {email}'

resultado = cadastro(nome='Alice', idade=30, email='alice@example.com')
print(resultado)


# kwargs para parâmetros nomeados
def funcao_com_parametros_nomeados(**pessoa):
    return pessoa

resultado = funcao_com_parametros_nomeados(nome='Bob', idade=25, email='bob@example.com', data_nascimento='01/01/1995')
print(resultado)

# Chamando a função usando um dicionário para passar os parâmetros nomeados
resultado = funcao_com_parametros_nomeados(**{'nome': 'Charlie', 'idade': 35})
print(resultado)

def funcao_com_parametros_nomeados_e_posicionais(a, b, **kwargs):
    print(f'Parâmetros posicionais: a={a}, b={b}')
    print(f'Parâmetros nomeados: {kwargs}')
    
funcao_com_parametros_nomeados_e_posicionais(1, 2, nome='David', idade=40)