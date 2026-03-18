'''
Peça ao usuário que informe um número. Percorra com um for até o número informado, e aplique potencia de 2 
  para os números pares, e potencia de 3 para os números ímpares. Imprima o resultado.
  
range(zero, numero_informado)
Exemplo: Se o usuário informar o número 5, o resultado deve ser:
1**3 = 1
2**2 = 4
3**3 = 27
4**2 = 16
5**3 = 125
'''
numero = int(input('Digite um número: '))
for contador in range(1, numero + 1):
    if contador % 2 == 0:
        print(f'{contador}**2 = {contador**2}')
    else:
        print(f'{contador}**3 = {contador**3}')