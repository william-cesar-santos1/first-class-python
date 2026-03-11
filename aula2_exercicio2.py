'''
Utilize o input para interação com o usuário. 
  Solicite o ano que este nasceu.
Calcule a idade aproximada do usuário e imprima a 
  mensagem: "Você tem X anos de idade", onde X é a idade calculada.
'''
ano_nascimento = int(input('Informe o ano que você nasceu: '))
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos de idade.')