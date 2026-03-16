'''
Peça ao usuário que informe a renda atual e o valor da parcela.
Com base nos dados informados, imprima se a parcela é maior 
  ou igual a 30% da renda.
'''
renda = float(input("Informe a renda atual: "))
parcela = float(input("Informe o valor da parcela: "))
percentual_parcela = (parcela / renda) * 100
parcela_maior_30 = percentual_parcela >= 30
print("A parcela é maior ou igual a 30% da renda:", parcela_maior_30)