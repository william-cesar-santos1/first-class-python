'''
Utilizando o conceito de clousure(funções aninhadas), crie uma função 
 que seja capaz de validar o usuário e senha de um sistema.
A função externa deve receber o nome de usuário e a senha corretos, 
  enquanto a função interna deve receber o nome de usuário e a senha 
  fornecidos pelo usuário e retornar True se forem válidos e False caso contrário.
'''
def validador_de_credenciais(usuario_correto, senha_correta):
    def validar(usuario_fornecido, senha_fornecida):
        return usuario_fornecido == usuario_correto \
            and senha_fornecida == senha_correta
    return validar
  
validador = validador_de_credenciais("admin", "1234")
print(validador("admin", "1234"))  # Saída: True
print(validador("admin", "wrong"))  # Saída: False
print(validador("user", "1234"))    # Saída: False