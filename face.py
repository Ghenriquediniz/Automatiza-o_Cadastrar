import tkinter as tk
import subprocess
import os
import signal

def iniciar_script():
    global processo
    if processo is None:
        processo = subprocess.Popen(['python', 'cadastrar.py'])

def parar_script():
    global processo
    if processo is not None:
        os.kill(processo.pid, signal.SIGTERM)
        processo = None

processo = None


janela = tk.Tk()
janela.title("Interface para Cadastrar.py")
janela.geometry("300x150") 


frame = tk.Frame(janela)
frame.pack(expand=True)


botao_iniciar = tk.Button(frame, text="Iniciar", command=iniciar_script, width=10)
botao_iniciar.pack(pady=10)


botao_parar = tk.Button(frame, text="Parar", command=parar_script, width=10)
botao_parar.pack(pady=10)


janela.mainloop()
