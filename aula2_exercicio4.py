'''
Calcule o consumo médio de combustível de um automóvel. 
  Para isso, o programa deve solicitar ao usuário a distância 
  percorrida (em km) e a quantidade de combustível 
  consumida (em litros). 
  Em seguida, o programa deve calcular e exibir o consumo 
  médio em km/l..
Para o calculo peça ao usuário quantos km ele percorreu e 
  quantos litros de combustível ele consumiu. 
  Depois, divida a distância percorrida pela quantidade de 
  combustível consumida para obter o consumo médio em km/l. 
  Por fim, exiba o resultado para o usuário.
'''
quilometros_percorridos = float(input('Informe a distância percorrida em km: '))
litros_consumidos = float(input('Informe a quantidade de combustível consumida em litros: '))
consumo_medio = quilometros_percorridos / litros_consumidos
print(f'O consumo médio do automóvel é: {consumo_medio} km/l')