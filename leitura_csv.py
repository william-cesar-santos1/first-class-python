import csv

def ler_csv(caminho_do_arquivo_csv):
    with open(caminho_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        linhas = csv.reader(arquivo)
        for linha in linhas:
            print(linha)

ler_csv('/Users/william/transacoes_bancarias.csv')