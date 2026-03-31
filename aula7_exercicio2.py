'''
Dados a lista de números a seguir, faça acesso posicional com tratamento de exceção para acessar o elemento 
  na posição inexistente.
'''
numeros = [10, 20, 30, 40, 50]

try:
    posicao = int(input("Digite a posição do número que deseja acessar: "))
    print(f'O número na posição {posicao} é: {numeros[posicao]}')
except IndexError:
    print("Erro: Posição inexistente na lista.")