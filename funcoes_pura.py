'''
Função pura é uma função que, para um mesmo conjunto de entradas, 
  sempre retorna o mesmo resultado e não tem efeitos colaterais observáveis. 
  Isso significa que a função não depende de nenhum estado externo e não modifica 
  nenhum estado externo.
'''
def somar(a, b):
    return a + b

print(somar(3, 5))

# Função impura
soma_total = 0
def somar(a, b):
    print(f"Somando {a} e {b}")
    global soma_total
    soma_total += a + b

somar(3, 5)
somar(10, 20)
print(f"Soma total: {soma_total}")

