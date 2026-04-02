'''
Utilize o conceito de clousure(funções aninhadas) para criar um contador de 
  chamadas de função. A função externa deve ser responsável por criar 
  e manter o contador, enquanto a função interna deve ser a função que será 
  chamada e que incrementará o contador a cada chamada. 
  Retorne a função interna para que ela possa ser utilizada como um contador 
  de chamadas.
'''

def contador_de_chamadas():
    contador = 0
    def incrementar_contador():
        global contador
        contador += 1
        return contador
    
    return incrementar_contador
  
contador = contador_de_chamadas()
print(contador())  # Saída: 1
print(contador())  # Saída: 2
print(contador())  # Saída: 3