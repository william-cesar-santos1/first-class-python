import csv

'''
O retorno da leitura do csv é uma lista de listas, onde cada linha do arquivo csv é representada 
  por uma lista de strings.
[
  0 = ['id_transacao', 'id_cliente', 'tipo_transacao', 'valor', 'data_transacao', 'conta_origem', 'conta_destino', 'descricao'],
  1 = ['1', '144', 'saque', '4938.32', '2025-02-06 03:23:00', 'Conta H', '', 'Saque'],
  2 = ['2', '143', 'deposito', '1314.72', '2025-02-20 18:45:00', 'Conta I', '', 'Depósito']
]
'''

def ler_csv(caminho_do_arquivo_csv):
    with open(caminho_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        linhas = csv.reader(arquivo)
        conteudo = list(linhas)
    return conteudo

try:
  conteudo = ler_csv('/Users/william/transacoes_bancarias.csv')
  print(conteudo)
except FileNotFoundError:
  print(f"O arquivo não foi encontrado.")
except Exception as e:
  print(f"Ocorreu um erro: {e}")