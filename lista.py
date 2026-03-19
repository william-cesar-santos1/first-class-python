'''
Lista é um tipo de coleção de dados no Python. Podem ser de tipos variados, ou seja, 
  uma lista pode conter números, strings, booleanos, etc.
As listas são mutáveis, ou seja, podem ser alteradas depois de criadas. Elas são definidas 
  usando colchetes [] e os elementos são separados por vírgulas.
  
Listas possuem indexação, ou seja, cada elemento tem um índice associado a ele, começando do 0.
'''
#          data(0),      valor(1),   descrição(2),               tipo(3),    conta_origem(4), conta_destino(5), status(6)
objetos = ['2026-03-18', 1514.00, 'Transação de depósito', 'Conta Corrente',   1234,            5678,          'successo']

matrix = [
  ['id_transacao', 'id_cliente', 'tipo_transacao', 'valor', 'data_transacao', 'conta_origem', 'conta_destino', 'descricao'],
  ['1', '144', 'saque', '4938.32', '2025-02-06 03:23:00', 'Conta H', '', 'Saque'],
  ['2', '143', 'deposito', '1314.72', '2025-02-20 18:45:00', 'Conta I', '', 'Depósito']
]
'''
Acessos a lista
'''
data = objetos[0]
print(data)

objetos[0] = '2026-03-19'

linha = int(input('Digite o número da linha: '))
coluna = int(input('Digite o número da coluna: '))
print(matrix[linha][coluna])


'''
Laços de repetição com listas
'''
for objeto in objetos:
    print(objeto, end=', ')
    
print('Percorrendo a matriz completa')
for linha in matrix:
    for coluna in linha:
        print(coluna, end=', ')
    print()
    

'''
Funções de uma lista
lista.append('elemento') - Adiciona um elemento ao final da lista.
lista.insert(1, 'elemento') - Adiciona um elemento em uma posição específica da lista.
lista.remove('elemento') - Remove a primeira ocorrência de um elemento da lista.
lista.pop(position) - Remove e retorna o elemento em uma posição específica da lista.
lista.clear() - Remove todos os elementos da lista.
lista.sort() - Ordena os elementos da lista.
lista.reverse() - Inverte a ordem dos elementos da lista.
len(lista) - Retorna o número de elementos da lista.
lista[position] = 'elemento' - Altera o elemento em uma posição específica da lista.
'''

alunos = ['Alice', 'Bob', 'Charlie']
alunos.append('David')
print(alunos)

'''
Laços de repetição com listas e enumerate
A função enumerate() é usada para obter o índice e o valor de cada elemento em uma lista
  durante um loop. Ela retorna um objeto enumerado, que pode ser convertido em uma lista
'''
for index, aluno in enumerate(alunos):
    print(f'{index}: {aluno}', end=', ')

'''
Pesquise se um elemento está presente em uma lista usando o operador in
for aluno in alunos:
  if aluno == 'William':
    print('William está presente na lista de alunos.')
'''
william_esta_present = 'William' in alunos
print(william_esta_present)

'''
Operações de slicing em listas
Slicing é uma técnica para obter uma sublista de uma lista. Ele é feito usando a`
'''
numero = [1,5,6,7,2,50,30,12,11,9]
print(f'Lista original: {numero}')
sub_lista = numero[:3]
print(f'Sublista inicio - 3: {sub_lista}')
sub_lista = numero[3:]
print(f'Sublista 3 - fim: {sub_lista}')
sub_lista = numero[6:10]
print(f'Sublista 6 - 10: {sub_lista}')

sub_lista = numero[0:8:2]
print(f'Sublista 0 - 8 - passo 2: {sub_lista}')

print(f'Lista ordenada: {sorted(numero)}')

