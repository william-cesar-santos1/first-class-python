'''
Peça ao usuário para informar a nota do aluno e também a 
  frequência nas aulas.
A frequência será informada em quantidade de aulas assistidas e o 
  total de aulas.
Para que o aluno seja reprovado, ele precisa ter uma nota 
  menor que 8 ou uma frequência menor que 85%.
No final da execução, imprima se o aluno foi reprovado: [True or False]
Disjunção lógica (or).
'''
nota = float(input("Informe a nota do aluno: "))
frequencia_assistida = int(input("Informe a quantidade de aulas assistidas: "))
frequencia_total = int(input("Informe a quantidade total de aulas: "))
frequencia = (frequencia_assistida / frequencia_total) * 100
if nota < 8 or frequencia < 85:
  print("O aluno foi reprovado!!!")
else:
  print("O aluno foi aprovado!!!")
print("Fim!!!")