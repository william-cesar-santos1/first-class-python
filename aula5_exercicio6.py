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

for chave, questao in questoes.items():
    # questão também é um dicionário, então podemos acessar suas chaves e valores
    print(questao['pergunta'])
    # opcoes é uma lista, você pode iterar sobre ela para mostrar as opções
    opcoes = questao['opcoes']
    print(opcoes)