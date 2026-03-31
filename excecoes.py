'''
Exceções são eventos que ocorrem durante a execução de um programa e que interrompem o 
  fluxo normal do programa.
'''
numero = None
while(numero is None):
    try:
        numero = int(input("Digite um número: "))
        print(f"O número digitado foi: {numero}")
    except ValueError:
        # Se deu erro no bloco try, o programa vai executar o bloco except
        print("O valor digitado não é um número válido.")