'''
Não mostrei a solução. É um desafio.

A nossa aplicação possui um número secreto. O número secreto é 42.
Peça que o usuário informe um número. Enquanto o número 
  informado for diferente do número secreto, continue pedindo 
  para o usuário informar um número.
'''
numero_secreto = 42
numero_informado = int(input("Digite um número: "))
while numero_informado > 0:
  if numero_informado == numero_secreto:
    print("Número correto! Parabéns!")
    break
  else:
    print("Número incorreto. Tente novamente.")
    numero_informado = int(input("Digite um número: "))