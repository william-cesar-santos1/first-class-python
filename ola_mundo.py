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

'''
O uso da palavra not no inicio da expressão logica, 
inverte o resultado da comparação.
not 5 != 2 -> False
not 5 == 2 -> True
not 5 > 2 -> False
not 5 < 2 -> True
'''

'''
Conjunção lógica: and
(5 > 2) [true] and (3 > 1) [true] -> True
(5 > 2) [true] and (3 < 1) [false] -> False
(5 < 2) [false] and (3 > 1) [true] -> False
(5 < 2) [false] and (3 < 1) [false] -> False
(5 > 2) [true] and (3 > 1) [true] and (2 == 2) [true] -> True
(5 > 2) [true] and (3 > 1) [true] and (2 == 3) [false] -> False

Tabela da verdade do operador and:
A     B     A and B
True  True  True
True  False False
False True  False
False False False
'''


'''
Disjunção lógica: or
(5 > 2) [true] or (3 > 1) [true] -> True
(5 > 2) [true] or (3 < 1) [false] -> True
(5 < 2) [false] or (3 > 1) [true] -> True
(5 < 2) [false] or (3 < 1) [false] -> False
(5 > 2) [true] or (3 > 1) [true] or (2 == 2) [true] -> True
(5 > 2) [true] or (3 > 1) [true] or (2 == 3) [false] -> True
(5 > 2) [true] or (3 < 1) [false] or (2 == 3) [false] -> True
(5 < 2) [false] or (3 > 1) [true] or (2 == 3) [false] -> True
(5 < 2) [false] or (3 < 1) [false] or (2 == 3) [false] -> False

Tabela da verdade do operador or:
A     B     A or B
True  True  True
True  False True
False True  True
False False False
'''

'''
Conjunção e disjunção lógica
(5 > 2) [true] and (3 > 1) [true] or (2 == 3) [false] -> True
(5 > 2) [true] and (3 < 1) [false] or (2 == 3) [false] -> False
(5 < 2) [false] and (3 > 1) [true] or (2 == 3) [false] -> False
(5 < 2) [false] and (3 < 1) [false] or (2 == 3) [false] -> False
(5 > 2) [true] and ((3 > 4) [false] or (2 == 2) [true]) -> True

(5 > 2) and (3 > 4 or 2 == 2)
(true ) and (false or true)
(true ) and (true)
true
'''

'''
truthy and falsy
Em Python, existem valores que são considerados verdadeiros (truthy) e valores que são considerados falsos (falsy) em contextos booleanos. 
Valores falsy incluem: False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)
Todos os outros valores são considerados truthy.

inteiro = 0 (falsy)
flutuante = 0.0 (falsy)
string_vazia = '' (falsy)
lista_vazia = [] (falsy)
tupla_vazia = () (falsy)
dicionario_vazio = {} (falsy)
conjunto_vazio = set() (falsy)
range_vazio = range(0) (falsy)

inteiro = 1 (truthy)
inteiro = -1 (truthy)
flutuante = 0.1 (truthy)
string = 'Olá' (truthy) 
lista = [1, 2, 3] (truthy)
tupla = (1, 2, 3) (truthy)
dicionario = {'chave': 'valor'} (truthy)
conjunto = {1, 2, 3} (truthy)
range = range(1) (truthy)
'''

'''
Condições / controle do fluxo de execução
if (se)
elif (senão se)
else (senão)
'''