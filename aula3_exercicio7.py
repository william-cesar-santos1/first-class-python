'''
Peça que o usuário informe a senha.
Enquanto a senha não seja igual 1234, continue pedindo para 
  o usuário informar a senha.
'''
senha = input("Digite a senha: ")
while senha != "1234":
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
print("Senha correta. Acesso concedido.")