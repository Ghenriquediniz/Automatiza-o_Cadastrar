import pyautogui as P
import os
from time import sleep
import keyboard
from PIL import Image

#Caminho das imagens
cadastro_path = ('img/cadastro.png')

cadastro_path = 'img/cadastro.png'

def clicar_cadastro(tentativas=5):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(cadastro_path, confidence=0.9)
            if posicao:
                P.click(P.center(posicao))
                print("Cliclicar_cadastro OK!")
                return
            else:
                print("Imagem não encontrada, tentando novamente...")
                sleep(1)
        except Exception as e:
            print(f"Erro ao procurar: {e}")
            sleep(1)
    raise Exception(f"Erro após {tentativas} tentativas.")

clicar_cadastro()