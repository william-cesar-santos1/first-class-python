'''
Faça um cadastro de funcionários, onde cada funcionário tem um nome e um salário.
Caso o usuário tente cadastrar um funcionário com um salário negativo, a função deve lançar uma exceção.

Lembre-se que o salário é um valor número (float) e trata a possibilidade do usuário inserir um valor que 
  não seja um número, tratando uma exceção apropriada.
'''
class SalarioInvalidoError(Exception):
    def __init__(self, salario, message="O salário deve ser um número positivo."):
        super().__init__(message)
        self.salario = salario

def cadastrar_funcionario():
    funcionario = None
    while(funcionario is None):
        try:
            nome = input("Digite o nome do funcionário: ")
            salario = float(input("Digite o salário do funcionário: "))
            if salario <= 0:
                raise SalarioInvalidoError(salario)
            funcionario = {"nome": nome, "salario": salario}
        except ValueError as e:
            print(f"Erro: O salário deve ser um número válido.")
        except SalarioInvalidoError as e:
            print(f"Erro: {e} (Salário informado: {e.salario})")
    return funcionario

funcionario_cadastrado = cadastrar_funcionario()
print(f"Funcionário cadastrado: {funcionario_cadastrado}")