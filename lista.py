'''
Lista é um tipo de coleção de dados no Python. Podem ser de tipos variados, ou seja, 
  uma lista pode conter números, strings, booleanos, etc.
As listas são mutáveis, ou seja, podem ser alteradas depois de criadas. Elas são definidas 
  usando colchetes [] e os elementos são separados por vírgulas.
  
Listas possuem indexação, ou seja, cada elemento tem um índice associado a ele, começando do 0.
'''
#          data(0),      valor(1),   descrição(2),               tipo(3),    conta_origem(4), conta_destino(5), status(6)
objetos = ['2026-03-18', 1514.00, 'Transação de depósito', 'Conta Corrente',   1234,            5678,          'successo']

for objeto in objetos:
    print(objeto, end=', ')
    
data = objetos[0]
print(data)

objetos[0] = '2026-03-19'
for objeto in objetos:
    print(objeto, end=', ')

print('\n')
matrix = [
  ['id_transacao', 'id_cliente', 'tipo_transacao', 'valor', 'data_transacao', 'conta_origem', 'conta_destino', 'descricao'],
  ['1', '144', 'saque', '4938.32', '2025-02-06 03:23:00', 'Conta H', '', 'Saque'],
  ['2', '143', 'deposito', '1314.72', '2025-02-20 18:45:00', 'Conta I', '', 'Depósito']
]
linha = int(input('Digite o número da linha: '))
coluna = int(input('Digite o número da coluna: '))
print(matrix[linha][coluna])

print('Percorrendo a matriz completa')
for linha in matrix:
    for coluna in linha:
        print(coluna, end=', ')
    print()