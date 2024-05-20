#Passo a passo do projeto

#1. Abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui

pyautogui.PAUSE = 0.4
import time


# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
time.sleep(1.3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(1.7)


#2. Fazer Login
pyautogui.click(x=510, y=383)
pyautogui.write("edu.python@rico.com")
pyautogui.press("tab")
pyautogui.write("1231231")
pyautogui.press("tab")
pyautogui.press("enter")

#3. Abri/importar lista de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

#5. Cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar em código do produto
    pyautogui.click(x=478, y=287)
    # escrever código do produto
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar para o próximo campo
    pyautogui.press("tab")
    # obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    # passar para o próximo campo
    pyautogui.press("tab")
    # apertar o botão
    pyautogui.press("enter") 
    #rolar tela para cima
    pyautogui.scroll(5000)
    


#5. Repetir isso tudo até acabar a lista de produtos
