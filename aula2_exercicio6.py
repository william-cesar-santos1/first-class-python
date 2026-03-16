'''
Peça ao usuário que informe um número aleatório.
Utilize o número informado e descubra se é um número par.
Imprima o seguinte texto: O número [número] é par: [True ou False]
Utilize o %
'''
numero = input('Informe um número aleatório: ')
numero_inteiro = int(numero)
numero_par = numero_inteiro % 2 == 0
print(f'O número {numero_inteiro} é par: {numero_par}')