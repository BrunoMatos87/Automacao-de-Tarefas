import pyautogui


pyautogui.PAUSE = 1 #pause de 1 segundo a cada ação de pyautogui
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
import time

# Passo 1: Entrar no sistema da empresa
# abrir navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(8)
print(pyautogui.position())
