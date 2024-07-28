import pyautogui as P
import os
from time import sleep
import keyboard


# Imagens
cadastro_path = 'img/cadastro.png'
cf_path = 'img/cf.png'
ind_path = 'img/ind.png'
pf_path = 'img/pf.png'
endereco_path = 'img/endereco.png'
cobranca_path = 'img/nome.png'

# Dados
dados_cadastros = "cadastros.txt"

# Cadastro
def clicar_cadastro(tentativas=5):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(cadastro_path, confidence=0.9)
            if posicao:
                P.click(P.center(posicao))
                print("Clicou no cadastro OK!")

                P.write(cnpj)
                P.press('tab')

                P.write(ie)
                P.press('tab')

                P.write(razao)
                P.press('tab')

                P.write(fantasia)

                return
            else:
                print("Imagem não encontrada, tentando novamente...")
                sleep(1)
        except Exception as e:
            print(f"Erro ao procurar: {e}")
            sleep(1)
    raise Exception(f"Erro após {tentativas} tentativas.")

# Marcar a atividade
def clicar_atividade(tentativas=5):
    if tipo_cliente == 'IND':
        path = ind_path
    elif tipo_cliente == 'CF':
        path = cf_path
    elif tipo_cliente == 'PF':
        path = pf_path
    else:
        raise ValueError("Tipo de cliente inválido. Use 'IND', 'CF' ou 'PF'.")

    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(path, confidence=0.9)
            if posicao:
                P.click(P.center(posicao))
                print("Clicou na atividade OK!")
                return
            else:
                print("Imagem não encontrada, tentando novamente...")
                sleep(1)
        except Exception as e:
            print(f"Erro ao procurar: {e}")
            sleep(1)

    raise Exception(f"Erro após {tentativas} tentativas.")

# Endereço
def clicar_endereco(tentativas=5):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(endereco_path, confidence=0.9)
            if posicao:
                P.click(P.center(posicao))
                print("Clicou no cadastro OK!")

                P.write(logra)
                P.press('tab')

                P.write(nu)
                P.press('tab')

                P.write(comple)
                P.press('tab')

                P.write(bairro)
                P.press('tab')

                P.write(muni)
                P.press('tab')

                P.write(uf)
                P.press('tab')

                P.write(pais)
                P.press('tab')

                P.write(cep)
                

                

                return
            else:
                print("Imagem não encontrada, tentando novamente...")
                sleep(1)
        except Exception as e:
            print(f"Erro ao procurar: {e}")
            sleep(1)
    raise Exception(f"Erro após {tentativas} tentativas.")

#Cobrança
def clicar_cobranca(tentativas=5):
    for _ in range(tentativas):
        try:
            posicao = P.locateOnScreen(cobranca_path, confidence=0.9)
            if posicao:
                P.click(P.center(posicao))
                print("Clicou no cadastro OK!")

                P.write(nome)
                P.press('tab')

                P.write(tel)
                P.press('tab')

                P.write(cell)
                P.press('tab')

                P.write(email)
                P.press('tab')   
                P.write(nada)
                P.press('enter')
                P.press('enter')

                return
            else:
                print("Imagem não encontrada, tentando novamente...")
                sleep(1)
        except Exception as e:
            print(f"Erro ao procurar: {e}")
            sleep(1)
    raise Exception(f"Erro após {tentativas} tentativas.")

with open(dados_cadastros) as arquivos:
    for linha in arquivos:
        partes = linha.split('*') 
        cnpj = partes[0]
        ie = partes[1]
        razao = partes[2]
        fantasia = partes[3]
        tipo_cliente = partes[4]
        logra = partes[5]
        nu = partes[6]
        comple = partes[7]
        bairro = partes[8]
        uf = partes[10]
        muni = partes[9]
        pais = partes[11]
        cep = partes[12]
        nome = partes[13]
        tel = partes[14]
        cell = partes[15]
        email = partes[16]
        nada = partes[17]


        try:
            clicar_cadastro()
            clicar_atividade()  # Passar o tipo_cliente como argumento
            clicar_endereco()
            clicar_cobranca()


        except Exception as e:
            print(f"Erro geral: {e}")
