import pyautogui
from pathlib import Path


# BASE_DIR = Path(__file__).resolve().parent.parent  # sai de /src
IMAGE_PATH = r"U:\AUTOMACAO\SAP\images\modulo.png"

print(IMAGE_PATH)  # debug opcional

pyautogui.FailSafeException # DESABILITA A AUTOMAÇÃO QUANDO O MOUSE FOR PARA O CANTO SUPERIOR ESQUERDO
pyautogui.sleep(2)  # espera 2 segundos para o usuário posicionar o mouse
pyautogui.locateOnScreen(IMAGE_PATH, confidence=0.8)
