'''
Peça ao usuário que informe um número aleatório.
Utilize o número informado e descubra se é um número par.
Caso seja par, imprima o texto: O número [número] é par.
Caso já seja ímpar, imprima o texto: O número [número] é ímpar.
'''
numero = int(input('Informe um número aleatório: '))
if (numero % 2) == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')