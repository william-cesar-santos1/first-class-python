'''
Peça ao usuário que informe um ano aleatório.
Utilize o ano informado e descubra se é um ano bissexto.
Anos bissextos são aqueles que são divisíveis por 4.
Caso seja bissexto, imprima o texto: O ano [ano] é bissexto.
Caso já não seja bissexto, imprima o texto: O ano [ano] não é bissexto.
'''
ano = int(input('Informe um ano aleatório: '))
if (ano % 4) == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')