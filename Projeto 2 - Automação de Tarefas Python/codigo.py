import pyautogui
import time

pyautogui.PAUSE = 0.5 # dar uma pausa de x segundos apos cada codigo realizado

#Passo 1 - entrar no sistema da empresa
pyautogui.press('win')  #pressionar uma tecla no teclado
pyautogui.write('chrome') #escrever um texto
pyautogui.press('enter')

# pyautogui.hotkey - pressionar uma combinação de tecla no teclado

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3) # dar tempo do site carregar

# Passo 2 - Fazer login

pyautogui.click(x=298, y=355) #clicando para escrever email

pyautogui.write("vini@email.com") #email
pyautogui.press('tab') #ir para senha
pyautogui.write("1234xasinjfsd") #senha

pyautogui.click(x=351, y=493) #clicando para logar
time.sleep(2) # dar tempo do site carregar

# Passo 3 - Importar a base de dados

# py -m pip install numpy
import pandas

tabela = pandas.read_csv('produtos.csv')
#lendo tabela em csv com Pandas e colocou na variavel tabela

# Passo 4 - Cadastrar 1 Produto
  #para cada linha da tabela
# Passo 5 - Repetir o processo de cadastro ate acabar

for linha in tabela.index:
  pyautogui.click(x=326, y=270) #clicando para cadastrar

  #codigo do produto
  codigo = tabela.loc[linha, 'codigo']
  pyautogui.write(codigo)
  pyautogui.press('tab') 

  #marca
  pyautogui.write(tabela.loc[linha, 'marca']) 
  pyautogui.press('tab') 

  #tipo
  pyautogui.write(tabela.loc[linha, 'tipo'])
  pyautogui.press('tab') 

  #categoria
  pyautogui.write(str(tabela.loc[linha, 'categoria']))
  pyautogui.press('tab') 

  # preço
  pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
  pyautogui.press('tab') 

  # custo
  pyautogui.write(str(tabela.loc[linha, 'custo']))
  pyautogui.press('tab') 

  #observação
  obs = tabela.loc[linha, 'obs']
  #verificando se esta vazio
  if not pandas.isna(obs): #se noa estiver vazio
    pyautogui.write(obs) #escrever a obs
  pyautogui.press('tab') 

  # enviar
  pyautogui.press('enter') 
  pyautogui.scroll(5000)


