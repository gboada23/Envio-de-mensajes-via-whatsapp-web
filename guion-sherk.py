import pyautogui as pt
from time import sleep

sleep(5)
def reemplazar_tildes(texto):
    """Reemplaza las tildes por sus códigos ASCII equivalentes."""
    return texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
i=0
with open('sherk.md', 'r',encoding='UTF-8') as txt:
    for fila in txt:
        if i < 45:
            pt.write(reemplazar_tildes(fila))  # Ensure UTF-8 encoding and decoding
            pt.press('enter')
            i+=1

