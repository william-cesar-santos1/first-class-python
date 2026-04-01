def ola_mundo(captura_nome):
    print(f"Olá, {captura_nome()}! Função por parametro")

def capturar_nome():
    return input("Digite seu nome: ")

x = ola_mundo
print(x)
x(capturar_nome)

# Clousure
def incrementar(inicial):
    def incremento_interno(incremento):
        return inicial + incremento
    return incremento_interno

incrementar_5 = incrementar(5)
print(f'Clousure - {incrementar_5(10)}')  # Isso deve imprimir 15 (5 + 10)
print(f'Clousure - {incrementar_5(20)}')  # Isso deve imprimir 25 (5 + 20)

# Funções anonimas (lambda)
# lambda parâmetros : expressão
soma = lambda a, b: a + b
print(f'Lambda - {soma(3, 5)}')  # Isso deve imprimir 8

capturar = lambda: f'Lambda - {input("Digite seu nome: ")}'
ola_mundo(capturar)