'''
Crie um função que seja um multiplicador base (função clousure).
A função deve receber um número como parâmetro e retornar outra função que, 
  por sua vez, deve receber outro número e retornar o resultado da multiplicação
  dos dois números.
'''
def multiplicador_base(x):
    def multiplicador(y):
        return x * y
    return multiplicador
  
multiplicador_por_2 = multiplicador_base(2)
print(multiplicador_por_2(5))  # Saída: 10
multiplicador_por_3 = multiplicador_base(3)
print(multiplicador_por_3(5))  # Saída: 15