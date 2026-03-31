'''
Escreva uma função que aplique a divisão entre dois números.
Adicione um tratamento de exceção para lidar com a divisão por zero, 
  retornando uma mensagem de erro apropriada.
'''

def dividir(numero_um, numero_dois):
    try:
        return numero_um / numero_dois
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    
try:
    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))
    print(f'{dividir(numero_um, numero_dois)=}')
except ValueError:
    print("Erro: Por favor, digite um número válido.")
