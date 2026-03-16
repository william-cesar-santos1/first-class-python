'''
Peça ao usuário para informar o valor total da compra.
Para compras cima de R$ 100,00, o cliente tem direito 
  a um desconto de 10%.
Exibe o novo valor da compra com o desconto aplicado, caso o cliente tenha direito.
'''
total = float(input('Informe o valor total da compra: '))
if total > 100:
    desconto = total * 0.10
    valor_com_desconto = total - desconto
    print(f'O valor da compra com o desconto aplicado é: R$ {valor_com_desconto:.2f}.')
else:
    print(f'O valor da compra é: R$ {total:.2f}. O cliente não tem direito ao desconto.')