print('Olá, mundo!')

# Variáveis
# Tipo de dado: inteiro
idade = 36
tipo_idade = type(idade)
print('O tipo de dado da variável idade é:', tipo_idade)
# Tipo de dado: float
salario = 1545.15
# Tipo de dado: string
nome = 'William César dos Santos'
# Tipo de dado: booleano (1 ou 0, verdadeiro ou falso)
estudante = False

'''
Este programa é um exemplo simples de como criar variáveis em Python e imprimir uma mensagem na tela.
As variáveis são usadas para armazenar informações que podem ser usadas posteriormente no programa.
'''

print('Meu nome é:', nome, 'e tenho a idade:', idade, sep=' ', end='\n')

#nome = input('Informe o seu nome: ')

'''
Operações aritméticas
Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Exponenciação: **
Módulo/Resto da divisão: %
'''
result = 5 % 2
print('O resultado do módulo é:', result)

numero_um = input('Informe o primeiro número: ')
numero_dois = input('Informe o segundo número: ')
print('A soma dos números é:', int(numero_um) + int(numero_dois))

'''
Operações lógicas
> maior que
< menor que
>= maior ou igual a
<= menor ou igual a
== igual a
!= diferente de

1 > 2 -> False
2 >= 1 -> True

2 < 1 -> False
2 <= 2 -> True
2 <= 1 -> False

1 == 1 -> True
1 == 2 -> False

1 != 2 -> True
1 != 1 -> False
'''

comparacao = 5 != 2
print('O resultado da comparação é:', comparacao)