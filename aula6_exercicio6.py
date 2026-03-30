'''
Crie uma função que ordene as palavras recebidas de forma crescente 
  ou decrescente, de acordo com um parâmetro adicional que indique a 
  ordem desejada.
'''
palavras = ['banana', 'abacaxi', 'laranja', 'uva', 'morango', 'abacate', 'kiwi', 'melancia', 'pera', 'cereja', 'amora', 'framboesa', 'goiaba', 'maracujá', 'pêssego', 'tangerina', 'caju', 'jabuticaba', 'graviola', 'acerola']
def ordenar_palavras(palavras, crescente=True):
    return sorted(palavras, reverse=not crescente)

print(f'ordenar palavras(crescente): {ordenar_palavras(palavras)}')
print(f'ordenar palavras(decrescente): {ordenar_palavras(palavras, False)}')
