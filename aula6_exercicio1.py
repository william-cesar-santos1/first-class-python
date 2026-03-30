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
nota_aprovacao = 80
frequencia_aprovacao = 85
nota_recuperacao = 60

resultado = {
    'aprovados': [],
    'recuperacao': [],
    'reprovados': []
}

def frequencia_percentual(frequencia, total_aulas):
    return (frequencia / total_aulas) * 100

def aprovado(nota, percentual_frequencia):
    return nota >= nota_aprovacao and percentual_frequencia >= frequencia_aprovacao
  
def recuperacao(nota, percentual_frequencia):
    return nota_recuperacao <= nota < nota_aprovacao and percentual_frequencia >= frequencia_aprovacao
  
def reprovacao(nota, percentual_frequencia):
    return nota < nota_recuperacao or percentual_frequencia < frequencia_aprovacao

# Solução com compreensão de listas
resultado = {
    'aprovados': [aluno['nome'] for classe in classes for aluno in classe['alunos'] 
                  if aprovado(aluno['nota'], frequencia_percentual(aluno['frequencia'], classe['total_aulas']))],
    'recuperacao': [aluno['nome'] for classe in classes for aluno in classe['alunos'] 
                    if recuperacao(aluno['nota'], frequencia_percentual(aluno['frequencia'], classe['total_aulas']))],
    'reprovados': [aluno['nome'] for classe in classes for aluno in classe['alunos'] 
                   if reprovacao(aluno['nota'], frequencia_percentual(aluno['frequencia'], classe['total_aulas']))]
}
print(f'Resultado com compreensão de listas: {resultado}')

resultado = {
    'aprovados': [],
    'recuperacao': [],
    'reprovados': []
}

for classe in classes:
    total_aulas = classe['total_aulas']
    for aluno in classe['alunos']:
        nome = aluno['nome']
        nota = aluno['nota']
        frequencia = aluno['frequencia']
        percentual_frequencia = frequencia_percentual(frequencia, total_aulas)
        
        if aprovado(nota, percentual_frequencia):
            resultado['aprovados'].append(nome)
        elif recuperacao(nota, percentual_frequencia):
            resultado['recuperacao'].append(nome)
        elif reprovacao(nota, percentual_frequencia):
            resultado['reprovados'].append(nome)
            
print(f'Resultado com loops: {resultado}')