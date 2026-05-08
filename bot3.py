import pyautogui
import time
from datetime import datetime


width, height = pyautogui.size()

conte = 0

pyautogui.moveTo(1500,600)

# 1380, 811 manga
# 1881, 1007 enviar
# 1382, 1007

contador = 0
quantidade = 100 

horario_atual = ''
while contador < quantidade:
    horario = """Nop"""
    print(horario, horario_atual)
    
    #if horario_atual != horario:
    horario_atual = horario
    pyautogui.moveTo(1534,1011)
    pyautogui.click()
    pyautogui.write(horario)
    pyautogui.click()
    pyautogui.moveTo(1380,811)
    pyautogui.click()
    pyautogui.moveTo(1881,1007)
    pyautogui.click()
    contador += 1

#while True:
#    print(pyautogui.position())