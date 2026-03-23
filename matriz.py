
matriz = [
  ['id_transacao', 'id_cliente', 'tipo_transacao', 'valor', 'data_transacao', 'conta_origem', 'conta_destino', 'descricao'],
  ['1', '144', 'saque', '4938.32', '2025-02-06 03:23:00', 'Conta H', '', 'Saque'],
  ['2', '143', 'deposito', '1314.72', '2025-02-20 18:45:00', 'Conta I', '', 'Depósito']
]

linha = int(input('Digite o número da linha: '))
coluna = int(input('Digite o número da coluna: '))
print(matriz[linha][coluna])

print('Percorrendo a matriz completa')
for linha in matriz:
    for coluna in linha:
        print(coluna, end=', ')
    print()
    