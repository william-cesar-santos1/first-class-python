'''
Gere um matriz de identidade de 4x4 usando listas aninhadas.
A matriz de identidade é uma matriz quadrada onde os elementos da diagonal 
  principal são iguais a 1 e os demais elementos são iguais a 0.
A matriz de identidade de 4x4 é a seguinte:
[
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
Utilize compreensão de listas para criar a matriz de identidade de 4x4.
'''
matriz_identidade = [[1 if linha == coluna else 0 
                      for coluna in range(4)] 
                     for linha in range(4)
                    ]
for linha in matriz_identidade:
    print(linha)