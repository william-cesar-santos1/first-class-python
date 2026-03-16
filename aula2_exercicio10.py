'''
Peça ao usuário que informe o valor total da compra e a 
  quantidade de parcelas.
Com esses dados, imprima o valor de cada parcela.
'''
total_compra = float(input("Informe o valor total da compra: "))
quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))
valor_parcela = total_compra / quantidade_parcelas
print(f"O valor de cada parcela é: R$ {valor_parcela}")