'''
Dado a frase abaixo. Conte quantas vezes cada palavra aparece na 
  frase e armazene essa informação em um dicionário.
Ignore letras maiúsculas e minúsculas, ou seja, "Meu" e "meu" devem 
  ser contados como a mesma palavra.
Exemplo:
frase = "Meu cachorro comeu o meu dever de casa"
Resultado esperado:
{
    "meu": 2,
    "cachorro": 1,
    "comeu": 1,
    "o": 1,
    "dever": 1,
    "de": 1,
    "casa": 1
}
'''
frase = "Meu cachorro comeu o meu dever de casa"
# Dicionário para armazenar a contagem de palavras
contagem_palavras = {}