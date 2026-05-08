"""
(1881,1007) # input de enviar
Point(x=1902, y=867) fora de tela

"""
from PIL import Image
import pytesseract
import pyscreenshot 
import pyautogui
from datetime import datetime
import re 
import os 
from datetime import datetime
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

WIDTH, HEIGHT = pyautogui.size()

texto_da_conversa = (1344,84,1920, 1080) # (x,y,x+largura da foto,y+altura da foto)
nome_do_perfil = (1410,84,1700,140)
parte_da_mensagem = (1370,920,1560,970)

#image = pyscreenshot.grab(bbox=parte_da_mensagem)
#image.show()

condicao = True

# envia uma mensagem
def saudacao(mensagem):

    try:
        pyautogui.moveTo(1534,1011) # input do chat
        pyautogui.click() # clica no chat

        if '\n' in mensagem:
            pyautogui.typewrite(mensagem)
        else:
            pyautogui.write(mensagem) # escreve mensagem
            pyautogui.press('enter')
  
        pyautogui.moveTo(1902,867) # move para fora da tela
        time.sleep(1)
        pyautogui.click() # clica no botao enviar
        time.sleep(1)
        
    except:
        ...

def captura_string(parte=0): # defina 0 para capturar a conversa ou 1 para capturar o nome de perfil
    # qual parte recortar para analisar

    recorte = texto_da_conversa if parte == 0 else nome_do_perfil if parte == 1 else parte_da_mensagem

    image = pyscreenshot.grab(bbox=recorte)
    msg = pytesseract.image_to_string(image)
    new_msg = re.sub(
        "\s[^a-zA-Z0-9]",
        "\n",
        msg
    ).lower()

    return new_msg

respondido = []

while condicao:

    # comandos para o bot
    if 'baom dia' in captura_string(0) and 'bom dia' not in respondido:
        dt = datetime.now()
        hora = dt.hour
        minuto = dt.minute
        segundo = dt.second
        saudacao(f'Bom dia meu nobre! E exatamente {hora}:{minuto}.')
        respondido.append('bom dia')

    if 'get horas' in captura_string(2):
        dt = datetime.now()
        hora = dt.hour
        minuto = dt.minute
        segundo = dt.second
        saudacao(f'{hora} horas e {minuto} minutos e {segundo} segundos.')
        #respondido.append('bom dia')
    
    if 'get nome' in captura_string(2):
        saudacao('Meu nome e GHOST por falta de criatividade do meu criador.')

    if 'oi' in captura_string(2):
        saudacao('Olá')
        
    if 'get comandos' in captura_string(2):
        comandos = """
        ====================================
        get nome | pergunta meu nome
        get horas | para informa a hora.
        get comandos | para ver os comandos.
        ====================================
        """
        saudacao(comandos)
    #time.sleep(3)
