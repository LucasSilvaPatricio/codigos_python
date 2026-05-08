from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import pyautogui 
from datetime import datetime
janela = webdriver.Chrome()

janela.get('https://web.whatsapp.com/')
pyautogui.sleep(35)

# envia mensagem
#    janela.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(grupo)
#    pyautogui.sleep(1)
#    pyautogui.press('enter')
#    pyautogui.sleep(1)
#    janela.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys('Texto enviado pelo Novo Bot')
#    pyautogui.sleep(1)
#    pyautogui.press('enter')

grupo = 'Teste'

def contatos_no_texto(lista,texto):
    retorno = False
    for contato in lista:
        if contato in texto:
            retorno = True
    
    return retorno
        
def gerador_de_id():
    dt = datetime.now()
    id_mensagem = f'{str(dt.hour)} + {str(dt.minute)} + {str(dt.second)}'
    return id_mensagem

def saudacao(mensagem):
    # envia mensagem
    #janela.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(grupo)
    #pyautogui.sleep(1)
    #pyautogui.press('enter')
    #pyautogui.sleep(1)
    
    janela.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(mensagem)
    pyautogui.sleep(1)
    pyautogui.press('enter')

# pega conversa do chat aberto
#print(janela.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]').text)

contatos = ['Anderson','Duda']

mensagem_temporarias = [['Teste',['#horas',0]],
                        ['Duda',['#horas',0]],
                        ['ANEE',['#horas',0]]]
horas = 0
nome = 0
tempo = 0
contador = 0
while True: 
    if contador == 0:
        texto = janela.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]').text
        horas = texto.count('#horas')
        nome = texto.count('#nome')
        contador = contador + 1

    try:                                        
                                              #//*[@id="main"]/div[2]/div/div[2]        
        
        
        texto = janela.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]').text

        print(f'{horas=} | {texto.count("#horas")}')
        print(f'{nome=} | {texto.count("#nome")}')
        #print(texto[0:-5])
        if horas > texto.count('#horas') or nome > texto.count('#nome'):
            horas = texto.count('#horas')
            nome = texto.count('#nome')
        

        if horas < texto.count('#horas') and '#horas' in texto[0:-5]:
            print('executando o hora')
            horas = texto.count('#horas')
            dt = datetime.now()
            horario = str(dt.hour)+':'+str(dt.minute) + ':' + str(dt.second)
            saudacao(f'São exatamente {horario}.')
        
        if nome < texto.count('#nome') and '#nome' in texto[0:-4] :
            print('executando o nome')
            nome = texto.count('#nome')
            saudacao('Sou um bot, me chamo bot do lucas.')
        
        
        
        """
        #print(texto)
        if '#horas' in texto and contatos_no_texto(contatos,texto): # verifica se existe o comando #horas e se quem enviou tá na lista de contatos permitidos
            
            # dados do usuario atual, para qual vai receber uma resposta
            nome_do_contato = ''

            for usuario in mensagem_temporarias:
                print(usuario)
                if texto.count(usuario[0]) > 0: # se o usuario procurado tiver no texto da mensagem
                    nome_do_contato = usuario[0] 
            print(f'{nome_do_contato=}')
            quantidade_de_mensagem = mensagem_temporarias[nome_do_contato][1]
            if quantidade_de_mensagem < texto.count('#horas'):  # verifica se a quantidade é menor do que a enviada
                mensagem_temporarias[nome_do_contato][1] = mensagem_temporarias[nome_do_contato][1] + 1
                
                dt = datetime.now()
                horario = str(dt.hour)+':'+str(dt.minute)
                saudacao(f'São exatamente {horario}!')
            """
        
    except Exception as error:
        print(error)
    time.sleep(1)

    
    
