'''
Dado um dicionario de questões. Crie umn programa capaz de interagir com 
  o usuário, fazendo as perguntas e verificando as respostas.
'''

questoes = {
    'questao1': {
        'pergunta': 'Qual é a capital da França?',
        'opcoes': ['Paris', 'Londres', 'Berlim', 'Roma'],
        'resposta': 'Paris'
    },
    'questao2': {
        'pergunta': 'Qual é a capital da Espanha?',
        'opcoes': ['Madri', 'Barcelona', 'Valência', 'Sevilha'],
        'resposta': 'Madri'
    },
    'questao3': {
        'pergunta': 'Qual é a capital da Itália?',
        'opcoes': ['Milão', 'Veneza', 'Roma', 'Florença'],
        'resposta': 'Roma'
    }
}

for chave, dicionario_questao in questoes.items():
    # questão também é um dicionário, então podemos acessar suas chaves e valores
    print(dicionario_questao['pergunta'])
    # opcoes é uma lista, você pode iterar sobre ela para mostrar as opções
    
    opcoes = dicionario_questao['opcoes']
    for index, opcao in enumerate(opcoes, start=1):
        print(f'{index} - {opcao}')
    
    opcao_escolhida = int(input('Digite o número da opção correta: '))
    
    resposta_correta = dicionario_questao['resposta']
    if opcoes[opcao_escolhida - 1] == resposta_correta:
        print('Resposta correta!')
    else:
        print('Resposta incorreta. A resposta correta é:', resposta_correta)
        
'''
Plus++++
Adicione uma contagem de acertos e erros para o usuário.
Aumente a quantidade de perguntas.
Se o usuário errar mais que três vezes, o programa deve encerrar.
'''