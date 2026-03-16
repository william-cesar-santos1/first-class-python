'''
Peça ao usuário para informar a nota do aluno e também a 
  frequência nas aulas.
A frequência será informada em quantidade de aulas assistidas e o 
  total de aulas.
Para que o aluno seja aprovado, ele precisa ter uma nota 
  maior ou igual a 8 e uma frequência maior ou igual a 85%.
Caso o aluno tenha nota inferior a 8. Porém acima de 6 e com 
  frequência maior ou igual a 85%, o aluno estará de recuperação.
  Se a frequência for inferior a 85%, o aluno estará reprovado,
Caso a nota do aluno seja inferior a 6, ele esta reprovado, 
  independente da frequência.
'''
nota = float(input('Informe a nota do aluno: '))
frequencia_assistida = int(input('Informe a quantidade de aulas assistidas: '))
frequencia_total = int(input('Informe a quantidade total de aulas: '))
frequencia = (frequencia_assistida / frequencia_total) * 100