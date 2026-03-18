'''
Peça ao usuário para informar um número aleatório.
  Calcule o fatorial usando while.
Exemplo:
Entrada: 5!
Saída: 5 x 4 x 3 x 2 x 1 = 120
'''
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = numero
while contador > 1:
    fatorial *= contador
    contador -= 1
print(f"{numero}! = {fatorial}")