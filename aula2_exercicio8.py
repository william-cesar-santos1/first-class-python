'''
Peça ao usuário para informar a nota do aluno e também a 
  frequência nas aulas.
A frequência será informada em quantidade de aulas assistidas e o 
  total de aulas.
Para que o aluno seja aprovado, ele precisa ter uma nota 
  maior ou igual a 8 e uma frequência maior ou igual a 85%.
No final da execução, imprima se o aluno foi aprovado: [True or False]
Conjunção lógica (and).
'''
nota = int(input("Informe a nota do aluno: "))
frequencia = int(input("Informe a frequência do aluno (quantidade de aulas assistidas): "))
total_aulas = int(input("Informe o total de aulas: "))
frequencia_percentual = (frequencia / total_aulas) * 100
if nota >= 8 and frequencia_percentual >= 85:
  print("O aluno foi aprovado!!!")
else:
  print("O aluno não foi aprovado!!!")
print("Fim!!!")