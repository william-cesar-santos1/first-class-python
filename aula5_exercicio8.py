'''
Dado a frase abaixo. Conte quantas vezes cada letra aparece na 
  frase e armazene essa informação em um dicionário.
Ignore letras maiúsculas e minúsculas, ou seja, "Meu" e "meu" devem 
  ser contados como a mesma letra.
Exemplo:
frase = "Meu cachorro comeu o meu dever de casa"
Resultado esperado:
{
    "m": 2,
    "e": 4,
    "u": 2,
    "c": 4,
    "a": 4,
    "h": 1,
    "r": 2,
    "o": 3,
    "d": 2,
    "v": 1,
    "s": 1
}
'''
frase = "Meu cachorro comeu o meu dever de casa"
# Dicionário para armazenar a contagem de palavras
contagem_palavras = {}
for letra in frase.lower():
    if letra in contagem_palavras:
        contagem_palavras[letra] += 1
    else:
        contagem_palavras[letra] = 1
print(contagem_palavras)