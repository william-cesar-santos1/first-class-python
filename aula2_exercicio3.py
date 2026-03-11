'''
Peça que ao usuário a temperatura atual(em Celsius) e 
  converta para Fahrenheit. 
A fórmula de conversão é: F = (C * 9/5) + 32
'''
graus_celsius = float(input('Informe a temperatura atual em Celsius: '))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32
print(f'A temperatura em Fahrenheit é: {graus_fahrenheit}°F')