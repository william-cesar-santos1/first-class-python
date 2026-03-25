'''
Dado a lista de alunos abaixo. Agrupe os alunos 
  aprovados, em recuperação e reprovados, utilizando um dicionário.
  
Regra de aprovação:
  nota >= 80 e frequência >= 85% -> Aprovado
  60 <= nota < 80 e frequência >= 85% -> Recuperação
  nota < 60 ou frequência < 85% -> Reprovado
  
{
  'aprovados': ['Alice', 'David', 'Grace', 'Judy'],
  'recuperacao': ['Bob', 'Heidi'],
  'reprovados': ['Charlie', 'Eve', 'Frank', 'Ivan']
}
'''
classes = [{
    'materia': 'Lógica de programação - PY',
    'total_aulas': 8,
    'alunos': [
        {'nome': 'Alice', 'nota': 85, 'frequencia': 7},
        {'nome': 'Bob', 'nota': 75, 'frequencia': 6},
        {'nome': 'Charlie', 'nota': 55, 'frequencia': 8},
        {'nome': 'David', 'nota': 90, 'frequencia': 2},
        {'nome': 'Eve', 'nota': 65, 'frequencia': 7},
        {'nome': 'Frank', 'nota': 45, 'frequencia': 5},
        {'nome': 'Grace', 'nota': 80, 'frequencia': 8},
        {'nome': 'Heidi', 'nota': 70, 'frequencia': 6},
        {'nome': 'Ivan', 'nota': 50, 'frequencia': 4},
        {'nome': 'Judy', 'nota': 95, 'frequencia': 9}
    ]
}]