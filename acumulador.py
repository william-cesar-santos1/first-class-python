def acumulador(inicial, quantidade, operacao):
    contador = 1
    acumulado = inicial
    while contador <= quantidade:
        acumulado = operacao(acumulado, contador)
        contador += 1
    return acumulado

somatorio = acumulador(0, 5, lambda x, y: x + y)
print(f'Somatório: {somatorio}')
fatorial = acumulador(1, 5, lambda x, y: x * y)
print(f'Fatorial: {fatorial}')