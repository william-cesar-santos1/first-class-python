'''
Faça uma média simples das notas informadas pelo usuário.
Peça ao usuário para informar um nota, enquanto a nota for maior que -1 continue.
  Quando o usuário informar uma nota menor que 0, pare de pedir as notas e imprima a média.
'''
contador = 0
soma = 0
nota = float(input("Digite uma nota (ou um número negativo para finalizar): "))
while nota >= 0:
    soma += nota
    contador += 1
    nota = float(input("Digite uma nota (ou um número negativo para finalizar): "))

if contador > 0:
    media = soma / contador
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi informada.")