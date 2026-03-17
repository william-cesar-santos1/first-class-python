numero = int(input('Digite um número: '))
contador = 0
while contador < numero:
    contador += 1
    if contador % 2 == 0:
        print(f'contador é par: ', end=' ')
    print(contador, end='\n')
print('Fim do loop crescente.')

'''
Faça um contador de forma decrescente, ou seja, do número 
informado pelo usuário até 0.
'''
contador = numero
while contador >= 0:
    print(contador, end='\n')
    contador -= 1
print('Fim do loop decrescente.')

idade = int(input('Digite a idade: '))
while idade < 0 or idade > 120:
    print('Idade inválida. Tente novamente.')
    idade = int(input('Digite a idade: '))
print('Idade válida. Fim do loop.')