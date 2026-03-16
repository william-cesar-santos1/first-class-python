'''
Peça ao usuário que informe dois números aleatórios.
Utilize os números informados e descubra se o primeiro número é maior que o segundo.
Caso seja, imprima o texto: O número [número1] é maior que o número [número2].
Caso já seja menor, imprima o texto: O número [número1] é menor que o número [número2].
'''
numero_um = float(input('Informe o primeiro número aleatório: '))
numero_dois = float(input('Informe o segundo número aleatório: '))
if numero_um > numero_dois:
    print(f'O número {numero_um} é maior que o número {numero_dois}.')
else:
    if numero_um == numero_dois:
        print(f'O número {numero_um} é igual ao número {numero_dois}.')
    else:
        print(f'O número {numero_um} é menor que o número {numero_dois}.')