'''
Você deve ter as libs do pyAutoGui e OpenCV instaladas,
para isso, instale via pip:

pyAutoGui:
>>> pip install pyautogui

OpenCV:
>>> pip install opencv-python
'''

import pyautogui

#Retorna um obj do tipo Box, exemplo: Box(left=1059, top=434, width=84, height=59)
#parametros(caminho da imagem, escala de cinza desabilitada, acurácia)
coord = pyautogui.locateOnScreen('./seis.png', grayscale=False, confidence = 0.9)

while coord == None:
    coord = pyautogui.locateOnScreen('./seis.png', grayscale=False, confidence = 0.9)
    print('procurando...')

#Retorna um obj do tipo Point, exemplo: Point(x=1441, y=582)
centro = pyautogui.center(coord)

#clica no Point
pyautogui.click(centro)

#Imprime as coordenadas
print(coord)
