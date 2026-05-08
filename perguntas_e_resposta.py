# Exercício - sistema de perguntas e respostas
import os 
import base64

os.system('cls')

perguntas = [
    {
        'Pergunta':'Qual o meu sobre nome?',
        'Opções':['Batista','Amorim','Patricio','Silva'],
        'Resposta' : 'U2lsdmE=',
    },
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 'NA==',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 'MjU=',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 'NQ==',
    },
]

pontuacao = 0

def imprimi_pergunta(item):
    print(item['Pergunta'])
    for indice, opcao in enumerate(item['Opções']):
        print(f'{indice})-{opcao}')

def valida_pergunta(resposta,opcoes):
    def verifica_acerto(jogada):
        global pontuacao
        if base64.b64decode(resposta).decode('utf-8') == opcoes[int(jogada)]:
            
            pontuacao = pontuacao + 1
            return 'Parabéns, você acertou!! 👍' 
        return 'Você errou ❌'
    return verifica_acerto

for item in perguntas:
    imprimi_pergunta(item)
    jogada = input('Qual a resposta?: ')

    if jogada.isdigit() and int(jogada) < len(item['Opções']):
        pergunta_validacao = valida_pergunta(item['Resposta'],item['Opções'])
        print(pergunta_validacao(jogada))
    else:
        print('Você errou!! 👍')
os.system('cls')
print('[+] ======= Fim de jogo ======= [+]')
print(f'Você acertou {pontuacao}/{perguntas.__len__()} 😏')
