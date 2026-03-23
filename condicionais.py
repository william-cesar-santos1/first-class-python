'''
Condicionais / controle do fluxo de execução
if (se)
elif (senão se)
else (senão)
'''
idade = int(input('Informe a sua idade: '))
if idade < 18:
    print('Você é menor de idade.')
elif idade >= 18 and idade < 65:
    print('Você é adulto.')
else:
    print('Você é idoso.')