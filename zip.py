'''
Zip é uma função embutida do Python que permite combinar elementos de 
  duas ou mais listas em uma única estrutura de dados. Ela retorna um 
  iterador de tuplas, onde cada tupla contém os elementos correspondentes 
  das listas fornecidas. O zip é útil para iterar sobre várias listas ao 
  mesmo tempo, facilitando a manipulação de dados relacionados.
A sintaxe básica do zip é a seguinte:
zip(lista1, lista2, ...)
Onde lista1, lista2, etc. são as listas que você deseja combinar. 
  O zip irá criar tuplas contendo os elementos correspondentes de cada lista. 
  Se as listas tiverem comprimentos diferentes, o zip irá parar quando a 
  menor lista for esgotada.
Exemplo de uso do zip:
'''
alunos = ['Alice', 'Bob', 'Charlie', 'Eve']
notas = [8.5, 7.0, 9.0]
'''
(Alice, 8.5), (Bob, 7.0), (Charlie, 9.0)
Note que o aluno "Eve" não foi incluído no resultado, pois a lista de 
  notas tem apenas 3 elementos, enquanto a lista de alunos tem 4 elementos.
'''
for aluno, nota in zip(alunos, notas):
    print(f'{aluno}: {nota}')