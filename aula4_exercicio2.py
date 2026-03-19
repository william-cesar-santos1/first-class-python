'''
Exercício: Pirâmide Centralizada com Asteriscos

Crie um programa em Python que:
  Peça ao usuário apenas: O tamanho da pirâmide (quantidade de linhas)
Utilize um for para imprimir uma pirâmide de asteriscos (*)
A pirâmide deve estar centralizada

Exemplo de saída para uma pirâmide de 4 linhas:

   *
  ***
 *****
*******
 '''
tamanho_piramide = int(input('Digite o tamanho da pirâmide (quantidade de linhas): '))
for index in range(1, tamanho_piramide + 1):
    espacos = ' ' * (tamanho_piramide - index)
    asteriscos = '*' * (2 * index - 1)
    print(espacos + asteriscos)